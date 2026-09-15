import requests

url = "https://api.chucknorris.io/jokes/random"
print(url)
result = requests.get(url)
print(f"Status code {str(result.status_code)}")
assert 200 == result.status_code
if result.status_code == 200:
    print("Success, get new joke")
else:
    print("Bab request")
result.encoding = "utf-8"
print(result.text)