import sqlite3

def delete_record(record_id):
    # Use the full path to your database
    conn = sqlite3.connect("/Users/chadelder/Documents/Python/RecordCollection/Vinyl/vinyl_collection.db")
    c = conn.cursor()
    c.execute("DELETE FROM records WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()
    print(f"Deleted record ID {record_id}")

# Example: delete record with ID 8
delete_record(10)


