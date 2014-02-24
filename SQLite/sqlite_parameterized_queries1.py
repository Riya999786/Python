## USE PARAMETERIZED QUERIES TO INSERT DATA - QUESTION MARK PLACEHOLDERS
# New data is stored in variables and is inserted into the query strings using parameters

import sqlite3 as lite
import sys

uId = 1
uPrice = 62300

con = lite.connect('test.db')

with con:

  cur = con.cursor()

  cur.execute("UPDATE Cars SET Price = ? WHERE Id = ?", (uPrice, uId))
  con.commit()

  print "Number of rows updated: %d" % cur.rowcount