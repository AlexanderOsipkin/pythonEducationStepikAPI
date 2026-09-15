import requests


class TestNewLocation:
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создаем 5 новых локаций и проверяем их"""

        base_url = "https://rahulshettyacademy.com"
        key = "?key=qaclick123"

        # POST
        post_resource = "/maps/api/place/add/json"  # Ресурс метода post

        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
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

        # Создаем текстовый файл и сохраняем в него place_id
        with open("../place_id.txt", "w") as file:

            # Создаем 5 новых локаций
            for i in range(5):
                print(f"Создание локации №{i + 1}")

                result_post = requests.post(post_url, json=json_for_create_new_location)
                print(f"Статус код POST: {result_post.status_code}")
                print(result_post.text)

                # Проверяем успешность POST
                assert result_post.status_code == 200

                check_post = result_post.json()
                check_info_post = check_post.get("status")
                print(f"Статус код ответа: {check_info_post}")

                assert check_info_post == "OK"
                print("Верный статус ответа")

                # Получаем place_id
                place_id = check_post.get("place_id")
                print(f"Получен place_id: {place_id}")

                # Проверяем, что place_id получен
                assert place_id

                # Сохраняем place_id в файл
                file.write(place_id + "\n")

        print("Все 5 place_id сохранены в файл place_id.txt")

        # GET
        """Проверка создания новых локаций"""

        get_resource = "/maps/api/place/get/json"  # Ресурс метода get

        # Читаем place_id из созданного файла
        with open("../place_id.txt", "r") as file:

            # Проверяем каждый place_id из файла
            for place_id in file:
                place_id = place_id.strip()
                print(f"Проверка place_id: {place_id}")

                full_place_id = f"&place_id={place_id}"

                get_url = base_url + get_resource + key + full_place_id
                print(get_url)

                result_get = requests.get(get_url)
                print(f"Статус код GET: {result_get.status_code}")
                print(result_get.text)

                # Проверяем, что локация существует
                assert result_get.status_code == 200

                if result_get.status_code == 200:
                    print(f"Локация с place_id {place_id} существует")
                else:
                    print(f"Локация с place_id {place_id} не найдена")

        print("Проверка всех 5 локаций завершена успешно")