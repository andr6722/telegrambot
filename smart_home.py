import telebot

from database import Database
from messages import START_MESSAGE
from status import status


class SmartHomeBot:
    def __init__(self, token, db_name):
        self.bot = telebot.TeleBot(token)
        self.db = Database(db_name)
        self.pending_login = {}

    def start(self, message):
        # Регистрация и авторизация пользователя
        user_id = message.from_user.id
        username = message.from_user.username
        self.bot.send_message(user_id, f'Добро пожаловать, {username}!')
        user = self.db.get_user(user_id)
        if not user:
            msg = self.bot.send_message(user_id, "Вы не зарегистрированы. Пожалуйста, введите пароль." )
            self.bot.register_next_step_handler(msg, self.registration)
        else:
            self.bot.send_message(user_id, "Вы уже зарегистрированы. Выполните вход с помощью /login.")

    def registration(self, message):

        user_id = message.from_user.id
        username = message.from_user.username
        password = message.text
        self.db.register_user(user_id, username, password)
        self.bot.send_message(message.chat.id, "Вы успешно зарегистрированы. Теперь выполните вход с помощью /login.")


    def request_login_password(self, user_id, message):
        self.pending_login[user_id] = self.db.get_user(user_id)
        self.bot.send_message(user_id, "Введите пароль для входа.")
        user_id = message.from_user.id
        if user_id in self.pending_login:
            entered_password = message.text
            if self.pending_login[user_id].verify_password(entered_password):
                self.bot.send_message(user_id, "Вход выполнен успешно.")
            else:
                self.bot.send_message(user_id, "Неверный пароль. Попробуйте снова.")
            del self.pending_login[user_id]
        else:
            self.bot.send_message(user_id, "Для выполнения входа введите пароль после команды /login.")

    def show_device_status():
        # Показать текущее состояние устройств в умном доме
        home_status = f"Температура: {status.temperature}C\n" \
                      f"Статус sds: {status.door_status}\n" \
                      f"Статус окон: {status.window_status}\n" \
                      f"Статус света: {status.light_status}"

    def control_device(self, message):
        # Управление устройствами в умном доме (например, свет, термостат)
        pass

    def create_automation(self, message):
        # Создание сценариев автоматизации (например, включение света при открытии двери)
        pass

    def schedule_device_control(self, message):
        # Возможность управления устройствами по расписанию
        pass
