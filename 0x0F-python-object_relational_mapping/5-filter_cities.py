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
    cur.execute("SELECT cities.name \
                 FROM cities \
                 JOIN states ON (cities.state_id = states.id) \
                 WHERE states.name = '{}' \
                 ORDER BY cities.id ASC".format(sys.argv[4]))
    records = cur.fetchall()
    print(', '.join([record[0]for record in records]))
    cur.close()
    db.close()
