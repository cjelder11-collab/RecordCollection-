import sqlite3

# Connect to your database
conn = sqlite3.connect("/Users/chadelder/Documents/Python/Vinyl/vinyl_collection.db")
c = conn.cursor()

# Delete rows where album is empty or NULL
c.execute("DELETE FROM records WHERE album IS NULL OR album = ''")
conn.commit()

print("Incomplete records removed from database.")

# Optional: show remaining records
c.execute("SELECT * FROM records")
rows = c.fetchall()
for row in rows:
    print(row)

conn.close()
