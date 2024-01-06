from django.db import models
from datetime import date

class Prescription(models.Model):
  patient_name = models.CharField(max_length=100, default="N/A") # Will turn into patient foreign key
  doctor_name = models.CharField(max_length=100, default="N/A") # Will turn into doctor foreign key
  issue_date = models.DateField(null=True, blank=True)
  expiry_date = models.DateField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True) # "YYYY-MM-DD"
  updated_at = models.DateTimeField(auto_now=True) # "YYYY-MM-DD"