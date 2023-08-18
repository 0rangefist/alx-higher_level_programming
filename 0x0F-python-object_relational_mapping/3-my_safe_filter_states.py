#!/usr/bin/python3
"""
This module takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument.
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

    # Query
    query = "SELECT * FROM states \
            WHERE name LIKE BINARY %s\
            ORDER BY id ASC"

    # Perform query (substituting in parameter)
    cur.execute(query, (argv[4],))

    # Get the rows of the query
    query_rows = cur.fetchall()

    # Print query results
    for row in query_rows:
        print(row)

    # Close the cursor & db connection
    cur.close()
    conn.close()
