import sqlite3

def initialize():
    con = sqlite3.connect("quotes.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS quotes
    (
    id INTEGER PRIMARY KEY,
    user STRING,
    quote STRING,
    quote_by STRING,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    cur.close()
    con.commit()

def validate_entry(user, quote, quote_by):
    return True

def add_entry(user, quote, quote_by):
    if validate_entry(user, quote, quote_by):
        con = sqlite3.connect("quotes.db")
        cur = con.cursor()
        cur.execute("""
        INSERT INTO quotes
        (
        user,
        quote,
        quote_by
        )
        VALUES(?, ?, ?)
        """,
        (user, quote, quote_by))
        cur.close()
        con.commit()

if __name__ == "__main__":
    initialize()