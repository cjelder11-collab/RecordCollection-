from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Vinyl Collection</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #f4f4f4; }
        table { width: 100%; border-collapse: collapse; background: white; }
        th, td { padding: 10px; border-bottom: 1px solid #ccc; text-align: left; }
        th { background: #333; color: white; }
        tr:hover { background: #eee; }
        h1 { font-size: 24px; }
    </style>
</head>
<body>
    <h1>🎵 Vinyl Collection</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>Artist</th>
            <th>Album</th>
            <th>Year</th>
            <th>Label</th>
        </tr>
        {% for row in rows %}
        <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
            <td>{{ row[3] }}</td>
            <td>{{ row[4] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

def get_records():
    conn = sqlite3.connect("/Users/chadelder/Documents/Python/Vinyl/vinyl_collection.db")
    c = conn.cursor()
    c.execute("SELECT id, artist, album, year, label FROM records")
    rows = c.fetchall()
    conn.close()
    return rows

@app.route("/")
def home():
    rows = get_records()
    return render_template_string(HTML, rows=rows)

if __name__ == "__main__":
    # 0.0.0.0 makes it available to your phone
    app.run(host="0.0.0.0", port=5000, debug=True)
