import requests
from utils.http_method import HttpMethods


"""Methods for test google maps API"""

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"
post_resource = "/maps/api/place/add/json"  # Ресурс метода post
get_resource = "/maps/api/place/get/json"  # Ресурс метода get


class GoogleMapsAPI:

    """Method create new location"""
    @staticmethod
    def create_new_place():
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

        post_url = base_url + post_resource + key
        print(post_url)

        result_post = HttpMethods.post(post_url, json_for_create_new_location)
        print(f"Статус код POST: {result_post.status_code}")
        print(result_post.text)
        return result_post

    """Method check new location"""
    @staticmethod
    def get_new_place(place_id):
        full_place_id = f"&place_id={place_id}"
        get_url = base_url + get_resource + key + full_place_id
        print(get_url)

        result_get = requests.get(get_url)
        print(f"Статус код GET: {result_get.status_code}")
        print(result_get.text)
        return result_get
