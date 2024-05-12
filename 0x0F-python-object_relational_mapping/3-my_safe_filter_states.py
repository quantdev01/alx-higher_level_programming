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
        name = args[4]
        query = "SELECT * FROM states WHERE BINARY name\
 LIKE %s ORDER BY id ASC"
        cursor.execute(query, (name + '%',))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Exception as e:
        print("This happend {}".format(e))
