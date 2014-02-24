## GETTING THE SQLITE3 VERSION
# Using WITH statement that checks 'con' variable (db connection) for errors and exits if any are encountered

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:

  cur = con.cursor()
  cur.execute('SELECT SQLITE_VERSION()')

  data = cur.fetchone()

  print "SQLite version: %s" % data