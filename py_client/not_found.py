import requests

endpoint = "http://localhost:8000/api/prescriptions/1000000/"

get_response = requests.get(endpoint)
print(get_response.json())