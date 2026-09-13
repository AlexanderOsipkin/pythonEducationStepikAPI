import requests


class TestNewLocation():
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создаем новую локацию"""

        base_url = "https://rahulshettyacademy.com"  # Базовый урл
        key = "?key=qaclick123"  # Параметр для всех запросов

        """POST"""
        post_resource = "/maps/api/place/add/json"  # Ресурс метода post

        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        print(result_post.text)

        assert result_post.status_code == 200
        if result_post.status_code == 200:
            print("Создана новая локация")
        else:
            print("Локация не создана. Получена ошибка")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print(f'Статус код ответа: {check_info_post}')
        assert check_info_post == "OK"
        print("Верный статус ответа")

        place_id = check_post.get("place_id")
        print(place_id)

        """GET"""

        """Проверка создания новой локации"""

        get_resource = "/maps/api/place/get/json"
        full_place_id = f'&place_id={place_id}'
        print(full_place_id)

        get_url = base_url + get_resource + key + full_place_id
        print(get_url)

        result_get = requests.get(get_url)
        print(result_get.text)

        assert result_get.status_code == 200
        if result_get.status_code == 200:
            print("Получена новая локация")
        else:
            print("Локация не получена. Получена ошибка")
