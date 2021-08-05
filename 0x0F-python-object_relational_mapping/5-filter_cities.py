#!/usr/bin/python3
"""list all cities of argument 4"""

import MySQLdb
from sys import argv
if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1],
                         port=3306,
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost")

    cursor = db.cursor()
    cursor.execute("SELECT cities.name\
    FROM cities\
    JOIN states\
    ON state_id=states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC", (argv[4],))

    data = cursor.fetchall()
    print(", ".join([r[0] for r in data]))

    cursor.close()
    db.close()
