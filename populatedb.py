import sqlite3
import sys
from settings import DB_NAME, DB_DATA

if len(sys.argv) >= 2:
    db_name = sys.argv[1]
else:
    db_name = DB_NAME

conn = sqlite3.connect(db_name)

with open(DB_DATA, "r") as fd:
    conn.executescript(fd.read())
    conn.commit()
