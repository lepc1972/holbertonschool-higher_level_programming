#!/usr/bin/python3
'''Script that list argument state in a safe way'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2],
                               db=argv[3])

    c = database.cursor()
    c.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
              [argv[4]])
    data = c.fetchall()
    for r in data:
        print(r)
    c.close()
    database.close()
