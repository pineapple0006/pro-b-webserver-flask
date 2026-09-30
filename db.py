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
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    cur.close()
    con.commit()

def validate_entry(user: str, quote: str, quote_by: str):
    return True if (len(quote) <= 600 and len(quote_by) <= 120 and len(quote_by) <= 120) else False

def add_entry(user: str, quote: str, quote_by: str):
    if not validate_entry(user, quote, quote_by): return

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

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_entries(search: str):
    search = ("%" if not search.startswith("%") else "") + search + ("%" if not search.endswith("%") else "")
    con = sqlite3.connect("quotes.db")
    con.row_factory = dict_factory
    cur = con.cursor()
    res = cur.execute("""
    SELECT * FROM quotes
    WHERE user LIKE ?
    OR quote LIKE ?
    OR quote_by LIKE ?
    ORDER BY id DESC
    """,
    (search, search, search)).fetchall()
    cur.close()
    con.commit()
    return res

if __name__ == "__main__":
    initialize()