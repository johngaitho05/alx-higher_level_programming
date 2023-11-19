#!/usr/bin/python3

import sys

import MySQLdb

if __name__ == '__main__':
    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host=host, port=port, user=user, password=password, database=database)
    cr = db.cursor()
    cr.execute("""SELECT id, name FROM states""")
    for rec in cr.fetchall():
        print(rec)
