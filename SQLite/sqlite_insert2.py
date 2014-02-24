## CREATES AND INSERTS DATA INTO DATABASE
# Assigns all data to be inserted into a list of tuples
# Table is destroyed if already exists and new one created
# executemany is used to insert all data from 'cars' list by using a parameterized string

import sqlite3 as lite
import sys

cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Citroen', 21000),
    (7, 'Hummer', 41400),
    (8, 'Volkswagen', 21600)
)

con = lite.connect('test.db')

with con:

  cur = con.cursor()

  cur.execute("DROP TABLE IF EXISTS Cars")
  cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
  cur.executemany("INSERT INTO Cars VALUES (?, ?, ?)", cars)