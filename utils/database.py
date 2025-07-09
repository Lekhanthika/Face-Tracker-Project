import sqlite3
import numpy as np
import datetime
import uuid

def init_db():
    conn = sqlite3.connect('face_tracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS visitors (
                  id TEXT PRIMARY KEY,
                  embedding BLOB,
                  first_seen TEXT,
                  last_seen TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  face_id TEXT,
                  timestamp TEXT,
                  event TEXT,
                  image_path TEXT
    )''')
    conn.commit()
    conn.close()

def get_all_embeddings():
    conn = sqlite3.connect('face_tracker.db')
    c = conn.cursor()
    c.execute("SELECT id, embedding FROM visitors")
    rows = c.fetchall()
    conn.close()

    embeddings = []
    for visitor_id, blob in rows:
        emb = np.frombuffer(blob, dtype=np.float32)
        embeddings.append((visitor_id, emb))
    return embeddings

def register_new_visitor(embedding):
    conn = sqlite3.connect('face_tracker.db')
    c = conn.cursor()
    visitor_id = str(uuid.uuid4())
    now = datetime.datetime.now().isoformat()
    emb_blob = embedding.astype(np.float32).tobytes()
    c.execute("INSERT INTO visitors (id, embedding, first_seen, last_seen) VALUES (?, ?, ?, ?)",
              (visitor_id, emb_blob, now, now))
    conn.commit()
    conn.close()
    return visitor_id

def update_last_seen(visitor_id):
    conn = sqlite3.connect('face_tracker.db')
    c = conn.cursor()
    now = datetime.datetime.now().isoformat()
    c.execute("UPDATE visitors SET last_seen = ? WHERE id = ?", (now, visitor_id))
    conn.commit()
    conn.close()
