from utils.api import GoogleMapsAPI
from utils.checking import Checking

"""Create, Update and delete location"""


class TestCreatePlace:

    def test_create_new_place(self):

        print("Method POST")
        result_post = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)

        print("Method GET")
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("Method PUT")
        result_put = GoogleMapsAPI.update_new_place(place_id)
        Checking.check_status_code(result_put, 200)

        print("Method GET after update")
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("Method DELETE")
        result_delete = GoogleMapsAPI.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)

        print("Method GET after delete")
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
