#!/usr/bin/python3
import MySQLdb
import sys

args = sys.argv

ln = len(args)

if ln < 4:
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
        # name = args[4]
        query = "select cities.id, cities.name, states.name from cities,\
 states where states.id = cities.state_id;"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Exception as e:
        print("This happend {}".format(e))
