from utils.http_method import HttpMethods


"""Methods for test google maps API"""

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"
post_resource = "/maps/api/place/add/json"  # Ресурс метода post
get_resource = "/maps/api/place/get/json"  # Ресурс метода get
put_resource = "/maps/api/place/update/json"  # Ресурс метода put
delete_resource = "/maps/api/place/delete/json"  # Ресурс метода delete


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
        print(f"Status code POST: {result_post.status_code}")
        print(result_post.text)
        return result_post

    """Method check new location"""
    @staticmethod
    def get_new_place(place_id):
        full_place_id = f"&place_id={place_id}"
        get_url = base_url + get_resource + key + full_place_id
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(f"Status code GET: {result_get.status_code}")
        print(result_get.text)
        return result_get

    """Method update new location"""
    @staticmethod
    def update_new_place(place_id):
        put_url = base_url + put_resource + key
        print(put_url)

        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        result_put = HttpMethods.put(put_url, json_for_update_new_location)
        print(f"Status code PUT: {result_put.status_code}")
        print(result_put.text)
        return result_put

    """Method delete new location"""

    @staticmethod
    def delete_new_place(place_id):
        delete_url = base_url + delete_resource + key
        print(delete_url)

        json_for_delete_new_location = {
            "place_id": place_id,
        }

        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_location)
        print(f"Status code DELETE: {result_delete.status_code}")
        print(result_delete.text)
        return result_delete