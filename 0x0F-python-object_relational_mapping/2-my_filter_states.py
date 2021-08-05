#!/usr/bin/python3
"""takes an argument and display the value"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}'\
    ORDER BY id ASC".format(argv[4]))
    states = cursor.fetchall()
    for st in states:
        if st[1] == argv[4]:
            print(st)
    cursor.close()
    db.close()
