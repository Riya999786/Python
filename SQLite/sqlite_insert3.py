## CREATES AND INSERTS DATA INTO DATABASE
# Assigns all sql queries into one multi-line comment block and executes via executescript method
# Commit method is used to manually commit changes since 'with' is not used
# TRY, EXCEPT, FINALLY statement is used
# If error is encountered, the changes are rolled back and an error is printed
# Database connection is closed after changes are completed successfully

import sqlite3 as lite
import sys

try:
  con = lite.connect('test.db')

  cur = con.cursor()

  cur.executescript("""
      DROP TABLE IF EXISTS Cars;
      CREATE TABLE Cars(Id INT, Name TEXT, Price INT);
      INSERT INTO Cars VALUES(1, 'Audi', 52642);
      INSERT INTO Cars VALUES(2, 'Mercedes', 57127);
      INSERT INTO Cars VALUES(3, 'Skoda', 9000);
      INSERT INTO Cars VALUES(4, 'Volvo', 29000);
      INSERT INTO Cars VALUES(5, 'Bentley', 350000);
      INSERT INTO Cars VALUES(6, 'Citroen', 21000);
      INSERT INTO Cars VALUES(7, 'Hummer', 41400);
      INSERT INTO Cars VALUES(8, 'Volkswagen', 21600);
      """)

  con.commit()

except lite.Error, e:

  if con:
    con.rollback()

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

  if con:
    con.close()