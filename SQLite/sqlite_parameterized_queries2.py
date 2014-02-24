## USE PARAMETERIZED QUERIES TO INSERT DATA - NAMED PLACEHOLDERS
# New data is stored in variables and is inserted into the query strings using parameters
# Results are gethered by the row and are printed by using list locations

import sqlite3 as lite
import sys

uId = 4

con = lite.connect('test.db')

with con:

  cur = con.cursor()

  cur.execute("SELECT Name, Price FROM Cars WHERE Id = :Id", {"Id": uId})
  con.commit()

  row = cur.fetchone()
  print row[0], row[1]