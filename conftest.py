import pytest
import random

@pytest.fixture
def generator_of_valid_password():
    password = f'{random.randint(100000, 999995)}'
    return password

@pytest.fixture
def generator_of_invalid_password():
    password = f'{random.randint(100, 995)}'
    return password

@pytest.fixture
def generator_of_login():
    login = f'andrewmaksimov46{random.randint(100, 995)}@yandex.ru'
    return login

@pytest.fixture
def registration_data_for_authorization():
    user_data = {
        'Имя' : 'Andrew',
        'Email' : 'andrewmaksimov46998@yandex.ru',
        'Пароль' : '999998'
    }
    
    return user_data