#!/usr/bin/python3
import MySQLdb
import sys

args = sys.argv

ln = len(args)

if ln <= 4:
    print("Insufusant arguments, need 3 args")

else:
    db = MySQLdb.connect(
            host="localhost",
            user=args[1],
            passwd=args[2],
            db=args[3],
            port=3306
            )

    cursor = db.cursor()

    try:
        query = "SELECT * FROM states WHERE BINARY name\
 LIKE '{}' ORDER BY id ASC".format(args[4])
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Exception as e:
        print("This happend {}".format(e))
