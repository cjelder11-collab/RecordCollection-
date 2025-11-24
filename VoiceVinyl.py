import sqlite3
import speech_recognition as sr

# --- Setup database ---
conn = sqlite3.connect("/Users/chadelder/Documents/Python/RecordCollection/Vinyl/vinyl_collection.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS records (
id INTEGER PRIMARY KEY AUTOINCREMENT,
artist TEXT,
album TEXT,
year TEXT,
label TEXT,
discogs_id TEXT
)
""")
conn.commit()

# --- Setup speech recognizer ---
r = sr.Recognizer()

print("🎵 Voice Vinyl Logger")
print("Say 'stop' at any prompt to quit.\n")

# --- Voice logging loop ---
while True:
    try:
        # --- Get artist ---
        with sr.Microphone() as source:
            print("Speak artist name:")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)

        artist = r.recognize_google(audio).strip().title()
        if artist.lower() == "stop":
            print("Stopping voice logging.")
            break
        print("Artist recognized:", artist)

        # --- Get album ---
        with sr.Microphone() as source:
            print("Speak album name:")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)

        album = r.recognize_google(audio).strip().title()
        if album.lower() == "stop":
            print("Stopping voice logging.")
            break
        print("Album recognized:", album)

        # --- Save to database ---
        c.execute(
            "INSERT INTO records (artist, album, year, label, discogs_id) VALUES (?, ?, ?, ?, ?)",
            (artist, album, None, None, None)
        )
        conn.commit()
        print(f"✔ Saved: {artist} - {album}\n")

    except sr.UnknownValueError:
        print("Didn't catch that. Try again.\n")
    except sr.RequestError as e:
        print("API error:", e, "\n")

# Close database connection
conn.close()
print("Database closed. Goodbye!")
