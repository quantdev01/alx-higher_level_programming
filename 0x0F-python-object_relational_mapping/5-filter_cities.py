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
        query = """SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
        cursor.execute(query, (name,))
        rows = cursor.fetchall()
        """for row in rows:
            print(row[0])
        """
        city_names = [row[0] for row in rows]
        print(", ".join(city_names))
    except Exception as e:
        print("This happend {}".format(e))
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
