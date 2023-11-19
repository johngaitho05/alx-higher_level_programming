#!/usr/bin/python3

import sys

import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(user=user, password=password, database=database)
    cr = db.cursor()
    cr.execute("""SELECT id, name FROM states""")
    for rec in cr.fetchall():
        print(rec)
