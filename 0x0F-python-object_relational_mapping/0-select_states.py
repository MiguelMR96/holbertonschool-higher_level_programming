#!/usr/bin/python3
"""
Select states from database
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3], charset="utf8")
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db_connection.close()
