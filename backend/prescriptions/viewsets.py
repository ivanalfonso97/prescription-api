from rest_framework import mixins, viewsets

from .models import Prescription
from .serializers import PrescriptionSerializer

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    lookup_field = 'pk'

class PrescriptionGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    '''
    get -> list
    get -> retrieve
    post -> create
    put -> update
    patch -> partial update
    delete -> destroy
    '''
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    lookup_field = 'pk'

prescription_list_view = PrescriptionGenericViewSet.as_view({'get': 'list'})
prescription_detail_view = PrescriptionGenericViewSet.as_view({'get': 'retrieve'})