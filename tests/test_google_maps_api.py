import json

from utils.api import GoogleMapsAPI
from utils.checking import Checking


class TestCreatePlace:
    """Create, Update and delete location"""

    def test_create_new_place(self):
        print("Method POST")
        result_post = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])

        print("Method GET")
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])

        print("Method PUT")
        result_put = GoogleMapsAPI.update_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])

        print("Method GET after update")
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])

        print("Method DELETE")
        result_delete = GoogleMapsAPI.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])

        print("Method GET after delete")
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])

        print("test_create_new_place PASSED")
