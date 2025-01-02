import requests

url = 'http://localhost:8000/items/'
data = [{'name': 'Item1'}, {'name': 'Item2'}, {'name': 'Item3'}]

for item in data:
    response = requests.post(url, json=item)
    print(response.json())
