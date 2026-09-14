import requests


class TestNewLocation:
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создаем 5 новых локаций, удаляем 2 и 4, проверяем и сохраняем существующие"""

        file_1 = "place_id.txt"
        file_2 = "place_id_2.txt"
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

        # Создаем текстовый файл и сохраняем в него 5 place_id
        with open(file_1, "w") as file:

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

        print(f"Все 5 place_id сохранены в файл {file_1}")

        # DELETE
        """Удалем 2 и 4 локацию"""

        delete_resource = "/maps/api/place/delete/json"  # Ресурс метода delete
        delete_url = base_url + delete_resource + key
        print(delete_url)

        # Читаем все 5 place_id из файла №1
        with open(file_1, "r") as file:
            place_ids = [place_id.strip() for place_id in file]

        # Удаляем 2 и 4 place_id
        for number in [2, 4]:
            place_id = place_ids[number - 1]
            print(f"Удаление локации №{number}")
            print(f"Place_id для удаления: {place_id}")

            json_for_delete_new_location = {
                "place_id": place_id
            }

            result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
            print(f"Статус код DELETE: {result_delete.status_code}")
            print(result_delete.text)

            # Проверяем успешность DELETE
            assert result_delete.status_code == 200

            check_delete = result_delete.json()
            check_delete_status = check_delete.get("status")
            print(f"Статус ответа DELETE: {check_delete_status}")

            assert check_delete_status == "OK"
            print(f"Локация №{number} успешно удалена")

        print("Локации 2 и 4 удалены")

        # GET
        """Проверка существующих и несуществующих локаций"""

        get_resource = "/maps/api/place/get/json"  # Ресурс метода get

        # Читаем place_id из файла №1
        with open(file_1, "r") as file:
            place_ids = [place_id.strip() for place_id in file]

        # Создаем файл №2 для существующих локаций
        with (open(file_2, "w") as file):

            # Проверяем каждый place_id из файла №1
            for i, place_id in enumerate(place_ids, start=1):
                print(f"Проверка локации №{i}")
                print(f"Place_id: {place_id}")

                full_place_id = f"&place_id={place_id}"
                get_url = base_url + get_resource + key + full_place_id
                print(get_url)

                result_get = requests.get(get_url)
                print(f"Статус код GET: {result_get.status_code}")
                print(result_get.text)

                # Проверяем существование локации
                if result_get.status_code == 200:
                    print(f"Локация №{i} существует")

                    # Сохраняем существующий place_id в файл 2
                    file.write(place_id + "\n")
                    print(f"Place_id {place_id} сохранен в {file_2}")

                elif result_get.status_code == 404:
                    print(f"Локация №{i} не существует")

                else:
                    print(f"Получен неожиданный статус код: {result_get.status_code}")
                    assert result_get.status_code in [200, 404]

        print("Проверка 5 локаций завершена")
        print(f"В файл {file_2} сохранены существующие локации")

        # GET
        """Проверка существующих локаций из второго файла"""

        # Читаем place_id из файла 2
        with open(file_2, "r") as file:
            place_ids = [place_id.strip() for place_id in file]
        print(f"Количество существующих place_id: {len(place_ids)}")

        # Проверяем, что после удаления осталось 3 локации
        assert len(place_ids) == 3
        print("Второй файл имеет все существующие place_id")

        # Проверяем каждый place_id из файла №2
        for place_id in place_ids:
            print(f"Повторная проверка place_id: {place_id}")

            full_place_id = f"&place_id={place_id}"
            get_url = base_url + get_resource + key + full_place_id
            print(get_url)

            result_get = requests.get(get_url)
            print(f"Статус код GET: {result_get.status_code}")
            print(result_get.text)

            # Проверяем, что локация существует
            assert result_get.status_code == 200
            print(f"Локация с place_id: {place_id} существует и корректна")

        print("Тест пройден успешно")