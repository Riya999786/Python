## RETRIEVE DATA FROM DATABASE - DICTIONARY
# Sets cursor to a dictionary style cursor
# Grabs data in all rows at once and prints row by row using the column id's (dictionary keys) through for loop

import sqlite3 as lite

con = lite.connect('test.db')

with con:

  con.row_factory = lite.Row

  cur = con.cursor()
  cur.execute("SELECT * FROM Cars")

  rows = cur.fetchall()

  for row in rows:
    print "%s %s %s" % (row["Id"], row["Name"], row["Price"])