import sqlite3
import sys
from settings import *

if len(sys.argv) > 1:
    DB_NAME = sys.argv[1]
    SQL_FILE = sys.argv[2]

conn = sqlite3.connect(DB_NAME)

with open(SQL_FILE, "r") as f:
    conn.executescript(f.read())
    conn.commit()
