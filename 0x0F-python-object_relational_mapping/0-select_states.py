#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    """
    Access to the database and get the states     from the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
