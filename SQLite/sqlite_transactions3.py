## TRANSACTIONS
# Friends table gets created if does not exists or deleted if it does
# No commit is explicitly called to write the data to the Friends table
# However, autocommit mode is implemented within the connection call
# This mode autocommits the data from the queries to the database

import sqlite3 as lite
import sys

try:
  con = lite.connect('test.db', isolation_level = None)
  cur = con.cursor()
  cur.execute("DROP TABLE IF EXISTS Friends")
  cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT)")
  cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
  cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
  cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
  cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")

except lite.Error, e:
  if con:
    con.rollback()

  print "Error %s:" % e.args[0]
  sys.exit(1)

finally:
  if con:
    con.close()