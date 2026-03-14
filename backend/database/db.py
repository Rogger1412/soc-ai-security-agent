import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # backend/database
DB_PATH = os.path.join(BASE_DIR, "..", "investigations.db")
DB_PATH = os.path.abspath(DB_PATH)

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS investigations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    target TEXT,
    intent TEXT,
    severity TEXT,
    score INTEGER,
    summary TEXT
)
""")

conn.commit()

print("Using database:", DB_PATH)