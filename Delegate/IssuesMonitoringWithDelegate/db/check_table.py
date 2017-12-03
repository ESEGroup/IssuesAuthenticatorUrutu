# Usage: python check_table.py tablename
import sys
import sqlite3
from datetime import datetime

tablename = sys.argv[1]
conn = sqlite3.connect('Issues.db')
cursor = conn.cursor()

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

#cursor.execute("INSERT INTO " + tablename + " (user_id, lab_id, data, chegada) VALUES (1,1,'"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"',1);")

print("Table " + tablename)
meta = cursor.execute("PRAGMA table_info('" + tablename + "')")
for r in meta:
    print(r)

print("\nEntries")
meta = cursor.execute("SELECT * FROM " + tablename)
for r in meta:
    print(r)
