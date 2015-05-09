#!/usr/bin/env python3
import sqlite3
import sys
from settings import DB_NAME, SQL_FILE

if len(sys.argv) >= 2:
    db_name = sys.argv[1]
    sql_file = sys.argv[2]
else:
    db_name = DB_NAME
    sql_file = SQL_FILE

conn = sqlite3.connect(db_name)

with open(sql_file, "r") as f:
    conn.executescript(f.read())
    conn.commit()
    conn.close()
