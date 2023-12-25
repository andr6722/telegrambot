import hashlib


class User:
    def __init__(self, user_id, username, password_hash):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash

    def verify_password(self, password):
        # Проверка пароля
        input_password_hash = hashlib.sha256(password.encode()).hexdigest()
        return input_password_hash == self.password_hash
