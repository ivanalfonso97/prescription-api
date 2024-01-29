from django.conf import settings 
from django.db import models
from datetime import date

User = settings.AUTH_USER_MODEL

class Prescription(models.Model):
  user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
  patient_name = models.CharField(max_length=100, default="N/A") # Will turn into patient foreign key
  doctor_name = models.CharField(max_length=100, default="N/A") # Will turn into doctor foreign key
  issue_date = models.DateField(null=True, blank=True)
  expiry_date = models.DateField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True) # "YYYY-MM-DD"
  updated_at = models.DateTimeField(auto_now=True) # "YYYY-MM-DD"