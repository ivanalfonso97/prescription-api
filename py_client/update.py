import requests

endpoint = "http://localhost:8000/api/prescriptions/3/update/"

data = {
  "doctor_name": "Paula"
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())