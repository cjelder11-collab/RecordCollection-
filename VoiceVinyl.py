import sqlite3
import speech_recognition as sr

# --- Setup database ---

conn = sqlite3.connect("/Users/chadelder/Documents/Python/Vinyl/vinyl_collection.db")
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
print("Speak the artist followed by the album (e.g., 'Bob Marley Exodus').")
print("Say 'stop' to quit.\n")

# --- Voice logging loop ---

while True:
    try:
        # all code that might raise an exception goes here
        with sr.Microphone() as source:
            print("Speak album information:")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)

        text = r.recognize_google(audio).strip()
        print("You said:", text)

        if text.lower() == "stop":
            print("Stopping voice logging.")
            break

        words = text.title().split()
        if len(words) < 2:
            print("❗ Please say at least artist and album.\n")
            continue

        artist = " ".join(words[:2])
        album = " ".join(words[2:]) if len(words) > 2 else None

        c.execute(
            "INSERT INTO records (artist, album, year, label, discogs_id) VALUES (?, ?, ?, ?, ?)",
            (artist, album, None, None, None)
        )
        conn.commit()
        print(f"✔ Saved: {artist} - {album if album else 'No album provided'}\n")

    except sr.UnknownValueError:
        print("Didn't catch that. Try again.\n")
    except sr.RequestError as e:
        print("API error:", e, "\n")




# Close database connection

conn.close()
print("Database closed. Goodbye!")
