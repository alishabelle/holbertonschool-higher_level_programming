#!/usr/bin/python3
""" script takes in argument and name matches the argument """

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
    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}' \
ORDER BY id ASC".format(sys.argv[4]))
    cur.execute(query)
    records = cur.fetchall()

    for record in records:
        print(record)

    cur.close()
    db.close()
