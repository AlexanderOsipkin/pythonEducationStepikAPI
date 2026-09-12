import requests


class TestNewJoke:
    """Tests for Chuck Norris jokes API"""

    def test_create_new_categories_joke(self):
        """Check that random joke with category can be created"""

        category = "sport"

        url = f"https://api.chucknorris.io/jokes/random?category={category}"
        print(f"Request URL: {url}")

        result = requests.get(url)
        print(f"Status code: {result.status_code}")

        assert result.status_code == 200
        print("Request successful")

        result.encoding = "utf-8"
        print(f"Response: {result.text}")

        check = result.json()
        check_info = check.get("categories")
        print(f"Categories: {check_info}")

        assert category in check_info
        print("Category correct")

        check_info_value = check.get("value")
        print(f"Joke: {check_info_value}")

        name = "Chuck Norris"
        if name in check_info_value:
            print("Name found")
        else:
            print("Name not found")


sport_joke = TestNewJoke()
sport_joke.test_create_new_categories_joke()
