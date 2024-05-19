import json


class Checking:
    """Метод для проверки ответов запроса"""
    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code
        print(f'Успешно статус код = {status_code}')

    @staticmethod
    def check_json_token(result, expected_value):
        """Метод для проверки наличия обязательных полей в ответе запроса"""
        token = json.loads(result.text)  # Получаем список полей
        assert expected_value == list(token)
        print('Все поля присутствуют')

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        """Метод для проверки значеинй обязательных полей в ответе запроса"""
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'{check_info} верно!')

    @staticmethod
    def check_search_word(result, field_name, search_word):
        """Метод проверки значений обязательных полей в ответе запроса по заданному слову"""
        check = result.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print('Проверка пройдена')
        else:
            print('Проверка не пройдена')


