import requests

endpoint = "http://localhost:8000/api"

answer = requests.get(endpoint)
print(answer.text)
print(answer.status_code)
print(answer.json()['message'])