import random

class Generators:

    @staticmethod
    def generate_of_valid_password():
        password = f'{random.randint(100000, 999995)}'
        return password

    @staticmethod
    def generate_of_invalid_password():
        password = f'{random.randint(100, 995)}'
        return password

    @staticmethod
    def generate_of_login():
        login = f'andrewmaksimov46{random.randint(100, 995)}@yandex.ru'
        return login
    