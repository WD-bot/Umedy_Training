import sqlite3
import datetime

db = sqlite3.connect("accounts.sqlite")

for row in db.execute("SELECT time_utc, account, amount, tz FROM history"):
    time_utc_str = row[0]
    tz_str = row[3]

    # Konverter UTC-streng tilbage til datetime
    utc_dt = datetime.datetime.strptime(time_utc_str, "%Y-%m-%d %H:%M:%S")
    utc_dt = utc_dt.replace(tzinfo=datetime.timezone.utc)

    # Konverter til lokal tid
    local_dt = utc_dt.astimezone()

    print(f"UTC: {utc_dt} | Local: {local_dt} | TZ stored: {tz_str}")

db.close()