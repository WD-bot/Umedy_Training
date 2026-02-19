import sqlite3
import datetime


DB_PATH = "accounts.sqlite"

db = sqlite3.connect(DB_PATH)
db.execute("PRAGMA foreign_keys = ON")

db.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    name TEXT PRIMARY KEY NOT NULL,
    balance INTEGER NOT NULL
)
""")

# Gem tid som TEXT (ISO 8601) og timezone som TEXT
db.execute("""
CREATE TABLE IF NOT EXISTS history (
    time_utc TEXT NOT NULL,
    account TEXT NOT NULL,
    amount INTEGER NOT NULL,
    tz TEXT NOT NULL,
    PRIMARY KEY (time_utc, account),
    FOREIGN KEY (account) REFERENCES accounts(name)
)
""")

# View der viser "lokal tid" baseret på systemets lokale timezone.
# Bemærk: SQLite kan kun lave 'localtime' conversion korrekt, hvis time_utc er i et format SQLite kan parse.
# ISO med "Z" eller +00:00 kan være tricky, derfor gemmer vi "YYYY-MM-DD HH:MM:SS" som UTC.
db.execute("""
CREATE VIEW IF NOT EXISTS localhistory AS
SELECT
    strftime('%Y-%m-%d %H:%M:%f', time_utc, 'localtime') AS localtime,
    account,
    amount,
    tz
FROM history
ORDER BY time_utc
""")

db.commit()


class Account:
    @staticmethod
    def _current_time_utc_and_tz() -> tuple[str, str]:
        """
        Returnerer:
          - UTC tid som tekst, SQLite-venligt format: 'YYYY-MM-DD HH:MM:SS'
          - Lokal timezone label (fallback: offset)
        """
        now_local = datetime.datetime.now().astimezone()
        tz = getattr(now_local.tzinfo, "key", None)  # fx 'Europe/Copenhagen' (kan mangle)
        if tz is None:
            tz = now_local.strftime("%z")  # fx '+0100'

        now_utc = now_local.astimezone(datetime.timezone.utc)
        # SQLite kan parse dette format stabilt med strftime(..., 'localtime')
        time_utc = now_utc.strftime("%Y-%m-%d %H:%M:%S")
        return time_utc, tz

    def __init__(self, name: str, opening_balance: int = 0):
        self.name = name

        row = db.execute(
            "SELECT name, balance FROM accounts WHERE name = ?",
            (name,)
        ).fetchone()

        if row:
            self.name, self._balance = row
            print(f"Retrieved record for {self.name}. ", end="")
        else:
            self._balance = opening_balance
            db.execute("INSERT INTO accounts(name, balance) VALUES(?, ?)", (name, opening_balance))
            db.commit()
            print(f"Account created for {self.name}. ", end="")

        self.show_balance()

    def _save_update(self, amount: int) -> None:
        new_balance = self._balance + amount
        time_utc, tz = Account._current_time_utc_and_tz()

        # Transaktion (så balance + history altid følges ad)
        with db:
            db.execute(
                "UPDATE accounts SET balance = ? WHERE name = ?",
                (new_balance, self.name)
            )
            db.execute(
                "INSERT INTO history(time_utc, account, amount, tz) VALUES(?, ?, ?, ?)",
                (time_utc, self.name, amount, tz)
            )

        self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0:
            self._save_update(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
            return amount / 100
        print("The amount must be greater than zero and no more than your account balance")
        return 0.0

    def show_balance(self) -> None:
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))


if __name__ == '__main__':
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()

    terry = Account("TerryJ")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    michael = Account("Michael")
    terryG = Account("TerryG")

    db.close()

