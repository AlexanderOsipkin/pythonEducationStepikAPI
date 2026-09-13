import requests


class TestNewLocation:
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создаем новую локацию"""

        base_url = "https://rahulshettyacademy.com"  # Базовый урл
        key = "?key=qaclick123"  # Параметр для всех запросов

        # POST
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

        # GET
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

        # PUT
        """Изменение новой локации"""

        put_resource = "/maps/api/place/update/json"

        put_url = base_url + put_resource + key
        print(put_url)

        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)

        assert result_put.status_code == 200
        if result_put.status_code == 200:
            print("Локация успешно обновлена")
        else:
            print("Локация не обновлена. Получена ошибка")

        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print(f'Сообщение: {check_put_info}')

        assert check_put_info == "Address successfully updated"
        print("Сообщение верно")

        """Проверка изменения новой локации"""

        result_get = requests.get(get_url)
        print(result_get.text)

        assert result_get.status_code == 200
        if result_get.status_code == 200:
            print("Проверка изменения локации прошла успешно")
        else:
            print("Проверка не прошла")

        check_address = result_get.json()
        check_address_info = check_address.get("address")
        print(f'Сообщение: {check_address_info}')

        assert check_address_info == "100 Lenina street, RU"
        print("Адрес верный")

        # DELETE
        """Удаление новой локации"""

        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)

        json_for_delete_new_location = {
            "place_id": place_id
        }

        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)

        assert result_delete.status_code == 200

        """Проверка удаления новой локации"""

        check_status = result_delete.json()
        check_status = check_status.get("status")
        print(f'Сообщение: {check_status}')

        assert check_status == "OK"
        print("Адрес удвлен")

        result_get = requests.get(get_url)
        print(result_get.text)

        assert result_get.status_code == 404
        if result_get.status_code == 404:
            print("Адрес удален успешно")
        else:
            print("Адрес не удален")