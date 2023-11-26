import sqlite3

from user import User


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # Создание таблицы для пользователей, устройств и сценариев автоматизации
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (id INTEGER PRIMARY KEY, user_id INTEGER, username TEXT)''')
        # Добавьте другие таблицы по необходимости

    def register_user(self, user_id, username):
        # Регистрация пользователя в БД
        self.cursor.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
        self.connection.commit()

    def get_user(self, user_id):
        # Получение информации о пользователе из БД
        self.cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        user = self.cursor.fetchone()
        if user:
            return User(user[1], user[2])
        else:
            return None
