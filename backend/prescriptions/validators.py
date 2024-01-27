from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Prescription

# def validate_patient_name(value):
#     queryset = Prescription.objects.filter(patient_name__iexact=value)
#     if queryset.exists():
#         raise serializers.ValidationError("Patient name must be unique")
#     return value
unique_patient_name_validator = UniqueValidator(
    queryset=Prescription.objects.all(), 
    message="Patient name must be unique",
    lookup='iexact'
)
