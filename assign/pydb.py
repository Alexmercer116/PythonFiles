import sqlite3 as sql

conn = sql.connect('emaildb.sqlite')
cur = conn.cursor()
