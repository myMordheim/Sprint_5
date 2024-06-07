import random
import secrets



class Registration():



    @staticmethod # Генерация рандомного логина
    def login():
        return f'artemkuznetsov9{random.randint(100, 999)}@yandex.ru'


    @staticmethod # Генерация рандомного валидного пароля
    def password():
        return secrets.token_urlsafe(6)


    @staticmethod # Генерация невалидного пароля
    def password_negative():
        return secrets.token_urlsafe(3)