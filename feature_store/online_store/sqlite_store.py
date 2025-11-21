import sqlite3
import json
import os

DB_PATH = "feature_store.db"

def init_db():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS online_features (
                        user_id TEXT PRIMARY KEY,
                        features_json TEXT
                    );
                   """)
    connection.commit()
    connection.close()

def write_features(user_id, fetaures_dict):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
            INSERT OR REPLACE INTO online_features (user_id, features_json)
            VALUES (?, ?)
    """, (user_id, json.dumps(fetaures_dict)))

    connection.commit()
    connection.close()

def read_features(user_id):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT features_json FROM online_features WHERE user_id = ?
    """, (user_id,))

    row = cursor.fetchone()
    connection.close()

    if row:
        return json.loads(row[0])
    return None


