#!/usr/bin/python3
""" print cities in their states """

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

    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON \
states.id=cities.state_id WHERE states.name = %s", (sys.argv[4],))
    records = cur.fetchall()
    store = []
    for record in records:
        store.append(record[0])
    print(','.join(store))
    cur.close()
    db.close()
