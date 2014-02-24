## DATA IMPORT FROM SQL FILE

import sqlite3 as lite
import sys

def readData():

  f = open('cars.sql', 'r')

  with f:
    data = f.read()
    return data

con = lite.connect(':memory:')

with con:

  cur = con.cursor()

  sql = readData()
  cur.executescript(sql)

  cur.execute("SELECT * FROM Cars")

  while True:

    row = cur.fetchone()

    if row == None:
      break

    print row[0], row[1], row[2]