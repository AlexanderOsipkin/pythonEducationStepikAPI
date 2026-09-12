import requests


class TestNewJoke:
    """Тесты для API Чака Норриса"""

    def test_create_jokes_by_all_categories(self):
        """Получаем случайную шутку по каждой категории"""

        # Получаем список всех доступных категорий
        categories_url = "https://api.chucknorris.io/jokes/categories"
        print(f"URL на получение категорий: {categories_url}")

        # Проверяем, что запрос категорий выполнен успешно
        categories_result = requests.get(categories_url)
        print(f"Статус код запроса категорий: {categories_result.status_code}")

        assert categories_result.status_code == 200
        print("Категории запрошены успешно")

        # Получаем информацию о категориях
        categories = categories_result.json()
        print(f"Полученные категории: {categories}")
        print(f"Количество категорий: {len(categories)}")

        # Проверяем, что категорий 16
        assert len(categories) == 16
        print("Количество категорий корректное")

        # Получаем по одной случайной шутке для каждой категории
        for category in categories:
            url = f"https://api.chucknorris.io/jokes/random?category={category}"

            print(f"Текущая категория: {category}")
            print(f"URL категории: {url}")

            # Проверяем, что шутка получена успешно
            result = requests.get(url)
            print(f"Статус код запроса: {result.status_code}")

            assert result.status_code == 200
            print("Шутки получена успешно")

            # Кодируем ответ в utf-8
            result.encoding = "utf-8"

            # Получаем категории из ответа
            check = result.json()
            check_info = check.get("categories")
            print(f"Категория в ответе: {check_info}")

            # Проверяем, что запрошенная категория есть в ответе
            assert category in check_info
            print("Категория в ответе корректная")

            # Получаем текст шутки
            check_info_value = check.get("value")
            print(f"Шутка про Чака Норриса: {check_info_value}")