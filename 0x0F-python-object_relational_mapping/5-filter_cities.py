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
    query = "SELECT cities.name \
            FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name = %s"

    # Perform query (substituting in parameter)
    cur.execute(query, (argv[4],))

    # Get the rows of the query
    query_rows = cur.fetchall()

    # Create a list to store city names
    city_names = [city[0] for city in query_rows]

    # Print query results
    print(', '.join(city_names))

    # Close the cursor & db connection
    cur.close()
    conn.close()
