import requests


class TestNewJoke:
    """Тесты для API Чака Норриса"""

    def test_create_joke_by_user_category(self):
        """Получаем шутку по категории которую ввел пользователь"""

        # Получаем категорию от пользователя
        category = input("Введите категорию шутки: ")

        # Получаем список всех доступных категорий
        categories_url = "https://api.chucknorris.io/jokes/categories"

        # Проверяем, что запрос категорий выполнен успешно
        categories_result = requests.get(categories_url)
        assert categories_result.status_code == 200

        # Получаем информацию о категориях
        categories = categories_result.json()

        # Проверяем, что выбранная пользователем категория есть на сайте
        if category not in categories:
            print(f"Категория '{category}' не найдена. Попробуйте ввести другую категорию.")
            return

        url = f"https://api.chucknorris.io/jokes/random?category={category}"

        # Проверяем, что шутка получена успешно
        result = requests.get(url)

        assert result.status_code == 200

        # Кодируем ответ в utf-8
        result.encoding = "utf-8"

        # Получаем категории из ответа
        check = result.json()
        check_info = check.get("categories")

        # Проверяем, что запрошенная категория есть в ответе
        assert category in check_info

        # Получаем текст шутки
        check_info_value = check.get("value")
        print(f"Шутка про Чака Норриса из категории {category}: {check_info_value}")