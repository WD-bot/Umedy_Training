import sqlite3


# db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES) #Old one
db = sqlite3.connect("accounts.sqlite")

for row in db.execute("""
    SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,
           history.account,
           history.amount
    FROM history
    ORDER BY history.time
"""):
    print(row)
    # # print(row)
    # local_time = row[0]
    # print("{}\t{}".format(local_time, type(local_time)))

db.close()