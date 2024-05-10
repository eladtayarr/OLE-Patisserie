import sqlite3

def create_database():
    # Connect to SQLite - This will create the database file if it doesn't exist
    conn = sqlite3.connect('user_database.db')

    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    # Create table as per requirement
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    # Commit your changes in the database
    conn.commit()

    # Close the connection
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def check_credentials(username, password):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

if __name__ == '__main__':
    create_database()
