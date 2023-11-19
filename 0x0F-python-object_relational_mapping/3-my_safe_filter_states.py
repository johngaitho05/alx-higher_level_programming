#!/usr/bin/python3
"""
This module  lists all states from the database hbtn_0e_0_usa
whose name matches the passed argument
It uses parametized query to prevent SQL injection
"""
import sys
import MySQLdb

if __name__ == '__main__':
    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    sname = sys.argv[4]
    db = None
    cr = None
    try:
        # Connect to the database
        db = MySQLdb.connect(host=host, port=port, user=user,
                             password=password, db=database, charset='utf8')
        cr = db.cursor()

        # Use parameterized query to prevent SQL injection
        query = """SELECT id, name FROM states WHERE BINARY
        name=%s ORDER BY id ASC"""
        cr.execute(query, (sname,))
        # Fetch and print results
        for rec in cr.fetchall():
            print(rec)

    except MySQLdb.Error as e:
        pass
    finally:
        # Close cursor and database connection
        if cr:
            cr.close()
        if db:
            db.close()
