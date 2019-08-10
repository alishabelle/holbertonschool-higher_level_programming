#!/usr/bin/python3
""" lists states in a database starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd="dub",
        db=sys.argv[3],
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%'"
    cur.execute(query)
    records = cur.fetchall()

    for record in records:
        print(record)

    cur.close()
    db.close()
