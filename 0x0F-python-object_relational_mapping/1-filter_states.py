#!/usr/bin/python3
import MySQLdb
import sys

args = sys.argv

ln = len(args)

if ln < 4:
    print("Insufusant arguments, need 3 args")

db = MySQLdb.connect(
        host="localhost",
        user=args[1],
        passwd=args[2],
        db=args[3],
        port=3306
        )

cursor = db.cursor()
try:
    cursor.execute("SELECT * from states WHERE BINARY name LIKE 'N%'")
    rows = cursor.fetchall()
except e:
    print("This happend {}".format(e))

for row in rows:
    print(row)
