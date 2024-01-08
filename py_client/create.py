import requests

endpoint = "http://localhost:8000/api/prescriptions/"

data = {
  "patient_name": "Juan",
  "doctor_name": "Paulo",
  "issue_date": "2023-05-01",
  "expiry_date": "2024-04-30",
}

get_response = requests.post(endpoint, data=data)
print(get_response.json())
