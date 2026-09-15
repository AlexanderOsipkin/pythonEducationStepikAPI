from utils.api import GoogleMapsAPI

"""Create, Update and delete location"""


class TestCreatePlace:

    def test_create_new_place(self):

        print("Method POST")
        result_post = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("Method GET")
        result_get = GoogleMapsAPI.get_new_place(place_id)

        print("Method PUT")
        result_put = GoogleMapsAPI.update_new_place(place_id)

        print("Method GET after update")
        result_get = GoogleMapsAPI.get_new_place(place_id)
