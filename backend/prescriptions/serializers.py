from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Prescription
from .validators import unique_patient_name_validator

class PrescriptionSerializer(serializers.ModelSerializer): 
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Prescription
        fields =  [
            'id',
            'url',
            'patient_name',
            'doctor_name',
            'issue_date',
            'expiry_date',
        ]
    
    patient_name = serializers.CharField(validators=[unique_patient_name_validator])
    # def validate_patient_name(self, value):
    #     queryset = Prescription.objects.filter(patient_name__iexact=value)
    #     if queryset.exists():
    #         raise serializers.ValidationError("Patient name must be unique")
    #     return value
    
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('prescription-detail', kwargs={'pk': obj.pk}, request=request)