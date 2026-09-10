# import requests

# api_key = "e78c17604cda35a59c09801f8d7d4dba"
# url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}"

# response = requests.get(url)

# print(response.status_code)
# print(response.json())

from pprint import pprint
import requests
r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=e78c17604cda35a59c09801f8d7d4dba")
pprint(r.json())