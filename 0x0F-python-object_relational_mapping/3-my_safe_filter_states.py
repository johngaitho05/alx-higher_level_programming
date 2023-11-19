#!/usr/bin/python3
"""
This module  lists all states from the database hbtn_0e_0_usa
whose name matches the passed argument and is safe from SQL injection
"""
import sys

import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cr = db.crsor()
    cr.execute("SELECT * FROM states WHERE name=%s\
            ORDER BY states.id", (sys.argv[4], ))

    for rec in cr.fetchall():
        print(rec)
    cr.close()
    db.close()
