import pytest
import random
import secrets


@pytest.fixture # Генерация рандомного логина
def login():
    return f'artemkuznetsov9{random.randint(100, 999)}@yandex.ru'


@pytest.fixture # Генерация рандомного валидного пароля
def password():
    return secrets.token_urlsafe(6)


@pytest.fixture # Генерация невалидного пароля
def password_negative():
    return secrets.token_urlsafe(3)

