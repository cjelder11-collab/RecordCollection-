import sqlite3

# Connect to the same database your voice script uses
conn = sqlite3.connect("/Users/chadelder/Documents/Python/Vinyl/vinyl_collection.db")  # absolute path recommended
c = conn.cursor()

# Fetch all records
c.execute("SELECT * FROM records")
rows = c.fetchall()

if rows:
    for row in rows:
        print(row)
else:
    print("No records found.")

conn.close()

# ---python3 view_records.py

