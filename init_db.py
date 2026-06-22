import sqlite3

conn = sqlite3.connect("queue.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database created successfully!")