## RETRIEVE DATA FROM DATABASE
# Grabs data in all rows at once and prints row by row through for loop
# Errors discovered in printout

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:

  cur = con.cursor()
  cur.execute("SELECT * FROM Cars")

  rows = cur.fetchall()

  for row in rows:
    print row