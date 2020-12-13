#!/usr/bin/python3
"""
Takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name
matches the argument.
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3], charset="utf8")

    cur = db_connection.cursor()

    cur.execute("SELECT * FROM states WHERE name='{}'\
                ORDER BY id ASC".format(sys.argv[4]))

    query_rows = cur.fetchall()

    for row in query_rows:
        if row[1] == sys.argv[4]:
            print(row)

    cur.close()
    db_connection.close()
