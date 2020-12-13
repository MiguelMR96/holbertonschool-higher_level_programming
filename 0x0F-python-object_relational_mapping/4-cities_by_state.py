#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3], charset="utf8")

    cur = db_connection.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states\
                ON states.id = cities.state_id ORDER BY cities.id")

    query_rows = cur.fetchall()

    for row in query_rows:
            print(row)

    cur.close()
    db_connection.close()
