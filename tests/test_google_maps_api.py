from utils.api import GoogleMapsAPI
from requests import Response

"""Create, Update and delete location"""


class TestCreatePlace:

    def test_create_new_place(self):

        print("Method POST")
        result_post: Response = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("Method GET")
        result_get: Response = GoogleMapsAPI.get_new_place(place_id)
