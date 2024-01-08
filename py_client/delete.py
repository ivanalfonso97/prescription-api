import requests

prescription_id = input("Enter prescription id: ")

try:
    prescription_id = int(prescription_id)
except:
    prescription_id = None
    print("Invalid id")

if prescription_id:
    endpoint = f"http://localhost:8000/api/prescriptions/{prescription_id}/delete/"

    get_response = requests.delete(endpoint)
    print(get_response.status_code)