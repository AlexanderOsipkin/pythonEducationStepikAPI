import requests


class TestNewJoke:
    """Tests for Chuck Norris jokes API"""

    def test_create_new_joke(self):
        """Check that random joke can be created"""

        url = "https://api.chucknorris.io/jokes/random"
        print(f"Request URL: {url}")

        result = requests.get(url)
        print(f"Status code: {result.status_code}")

        assert result.status_code == 200
        print("Request successful")

        result.encoding = "utf-8"
        print(f"Response: {result.text}")

        check = result.json()  # задаем переменную для парсинга результата
        check_info = check.get("categories")  # Проверяем что у поля категории в ответе приходят []
        print(check_info)
        assert check_info == []
        print("Categories correct")

        check_info_value = check.get("value")
        print(check_info_value)
        # Задаем переменную и проверяем есть ли она в поле value
        name = "Chuck Norris"
        if name in check_info_value:
            print("Name found")
        else:
            print("Name not found")


random_joke = TestNewJoke()
random_joke.test_create_new_joke()

