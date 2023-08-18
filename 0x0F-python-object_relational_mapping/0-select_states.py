#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    #  Connect to the MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8")

    # Start cursor
    cur = conn.cursor()

    # Perform query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Get the rows of the query
    query_rows = cur.fetchall()

    # Print query results
    for row in query_rows:
        print(row)

    # Close the cursor & db connection
    cur.close()
    conn.close()
