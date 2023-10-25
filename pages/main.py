import requests
import json

url = "https://anime-db.p.rapidapi.com/anime"
querystring = {"page": "1", "size": "25500", "sortBy": "ranking"}

headers = {
    "X-RapidAPI-Key": "a21ad9bc0emsh054cbd0252ecc89p188720jsnfd36f6e8e142",
    "X-RapidAPI-Host": "anime-db.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json()
    with open('anime_data.json', 'w') as json_file:
        json.dump(data, json_file)
    print("Response saved to anime_data.json")
else:
    print("Request failed with status code:", response.status_code)
