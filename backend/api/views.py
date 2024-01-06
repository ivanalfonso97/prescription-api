import json
from django.http import JsonResponse

from prescriptions.models import Prescription

def api_home(request, *args, **kwargs):
    model_data = Prescription.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = {
            "id": model_data.id,
            "patient_name": model_data.patient_name,
            "doctor_name": model_data.doctor_name,
            "issue_date": model_data.issue_date,
            "expiry_date": model_data.expiry_date,
            "created_at": model_data.created_at,
            "updated_at": model_data.updated_at,
        }
    return JsonResponse(data)