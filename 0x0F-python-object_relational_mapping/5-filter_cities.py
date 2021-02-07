#!/usr/bin/python3
""" script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name \
        FROM cities \
        INNER JOIN states \
        ON state_id=states.id \
        WHERE states.name='{}' \
        ORDER BY cities.id ASC".format(sys.argv[4]))
    data = cursor.fetchall()
    result = []
    for i in data:
        result.append(i[0])
    print(", ".join(result))
    cursor.close()
    db.close()
