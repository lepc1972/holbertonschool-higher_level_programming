#!/usr/bin/python3
''' this Script lists all states from database hbtn_0e_0_usa'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2],
                               db=argv[3])

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    data = cursor.fetchall()
    for r in data:
        if r[1].startswith("N"):
            print(r)
    cursor.close()
    database.close()
