import sqlite3
import hashlib
from user import User


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.create_table()

    def create_connection(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                        (id INTEGER PRIMARY KEY, user_id INTEGER, username TEXT, password_hash TEXT)''')
        connection.commit()
        connection.close()

    def register_user(self, user_id, username, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (user_id, username, password_hash) VALUES (?, ?, ?)", (user_id, username, password_hash))
        connection.commit()
        connection.close()

    def get_user(self, user_id):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        user = cursor.fetchone()
        connection.close()
        if user:
            return User(user[1], user[2], user[3])
        else:
            return None