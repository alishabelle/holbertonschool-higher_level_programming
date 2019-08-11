#!/usr/bin/python3
""" lists all cities in database """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
INNER JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC"
    cur.execute(query)
    records = cur.fetchall()

    for record in records:
        print(record)

    cur.close()
    db.close()
