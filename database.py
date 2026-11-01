import sqlite3
from datetime import datetime

def connect_db():
    return sqlite3.connect("phishing_history.db")


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    # Email history
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            prediction TEXT,
            analyzed_at TEXT
        )
    """)

    # URL history
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS url_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            risk_score INTEGER,
            result TEXT,
            analyzed_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_email(email, prediction):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO email_history
        (email, prediction, analyzed_at)
        VALUES (?, ?, ?)
    """, (
        email,
        prediction,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_history():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM email_history ORDER BY id DESC
    """)

    records = cursor.fetchall()
    conn.close()

    return records


# Save URL analysis
def save_url(url, risk_score, result):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO url_history
        (url, risk_score, result, analyzed_at)
        VALUES (?, ?, ?, ?)
    """, (
        url,
        risk_score,
        result,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


# Retrieve URL history
def get_url_history():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM url_history ORDER BY id DESC
    """)

    records = cursor.fetchall()
    conn.close()

    return records