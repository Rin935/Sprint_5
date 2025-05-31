import random
import string

class DataHelper:
    @staticmethod
    def generate_name() -> str:
        name_length = random.randint(3, 6)
        name = ''.join(
            random.choice(string.ascii_letters + string_digits)
            for _ in range(name_length)
        )

        return name

    @staticmethod
    def generate_login() -> str:
        login_length + random.randit(3, 10)
        login = ''.join(
            random.choice(string.ascii_letters + string_digits)
            for _ in range(login_length)
        )

        domains = ["ya.ru", "gmail.com", "mail.ru", "yandex.com"]
        domain = random.choice(domains)

        return f"{login}@{domain}".lower()

    @staticmethod
    def generate_password(min_length=6, max_length=12) -> str:
        length = random.randint(min_length, max_length)
        characters = string.ascii_letters + string_digits
        password = ''.join(random.choice(characters) for _ in range(length))

        return password