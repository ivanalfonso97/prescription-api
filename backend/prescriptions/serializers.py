from rest_framework import serializers

from .models import Prescription

class PrescriptionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Prescription
        fields =  [
            'id',
            'patient_name',
            'doctor_name',
            'issue_date',
            'expiry_date',
        ]