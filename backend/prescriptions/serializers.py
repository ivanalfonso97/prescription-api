from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer

from .models import Prescription
from .validators import unique_patient_name_validator

class PrescriptionSerializer(serializers.ModelSerializer): 
    owner = UserPublicSerializer(source='user', read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Prescription
        fields =  [
            'owner',
            'id',
            'url',
            'edit_url',
            'patient_name',
            'doctor_name',
            'issue_date',
            'expiry_date',
        ]
    
    patient_name = serializers.CharField(validators=[unique_patient_name_validator])
    
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('prescription-detail', kwargs={'pk': obj.pk}, request=request)
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('prescription-edit', kwargs={'pk': obj.pk}, request=request)