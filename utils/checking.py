"""Methods for assert responce"""


class Checking:
    """Method for check status code"""

    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, 'Error, stratus code not assert'
        print(f"Success! Status code = {result.status_code}")
