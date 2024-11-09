import sqlite3

DATABASE_NAME = "network_data.db"
# SQLite database URL
DATABASE_URL = f"sqlite:///./{DATABASE_NAME}"

# Connect to SQLite database
def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name (like a dictionary)
    return conn

# Initialize database and create a table if it doesn't exist
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS network_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT NOT NULL,  -- Now accepting time as text (string or datetime)
            source_ip TEXT NOT NULL,
            destination_ip TEXT NOT NULL,
            protocol TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

