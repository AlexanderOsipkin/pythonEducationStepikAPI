import json

"""Methods for assert response"""


class Checking:

    @staticmethod
    def check_status_code(result, status_code):
        """Method for check status code"""
        assert status_code == result.status_code, 'Error, stratus code not assert'
        print(f"Success! Status code = {result.status_code}")

    @staticmethod
    def check_json_token(result, expected_value):
        """Method for check json in response"""
        fields = json.loads(result.text)
        assert list(fields) == expected_value, 'Error, json have not required fields'
        print(list(fields))
        print("All fields are present")
