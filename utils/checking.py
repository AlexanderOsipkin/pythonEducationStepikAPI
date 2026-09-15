import json

"""Methods for assert response"""


class Checking:
    """Method for check status code"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, 'Error, stratus code not assert'
        print(f"Success! Status code = {result.status_code}")

    """Method for check json in response"""
    @staticmethod
    def check_json_token(result, expected_value):
        fields = json.loads(result.text)
        assert list(fields) == expected_value, 'Error, json have not required fields'
        print(list(fields))
        print("All fields are present")

    """Method for check json value"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(check_info)
        print(f"{field_name} present")

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        """Method for checking the values of required fields in a request response"""
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f"Word {search_word} present")
