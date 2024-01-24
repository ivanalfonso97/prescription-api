from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.mixins import StaffEditorPermissionMixin

from .models import Prescription
from .serializers import PrescriptionSerializer

# class PrescriptionListAPIView(generics.ListAPIView):
#   queryset = Prescription.objects.all()
#   serializer_class = PrescriptionSerializer

# prescription_detail_view = PrescriptionListAPIView.as_view()

class PrescriptionListCreateAPIView(
    # StaffEditorPermissionMixin,
    generics.ListCreateAPIView
):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
  
    def perform_create(self, serializer):
        # patient_name = serializer.validated_data.get('patient_name') or None
        doctor_name = serializer.validated_data.get('doctor_name') or None

        # if patient_name is None:
        #   raise ValidationError("Patient name is required")
        if doctor_name is None:
            doctor_name = "N/A"
        
        serializer.save()

prescription_list_create_view = PrescriptionListCreateAPIView.as_view()

class PrescriptionDetailAPIView(
    # StaffEditorPermissionMixin,
    generics.RetrieveAPIView
):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

prescription_detail_view = PrescriptionDetailAPIView.as_view()

class PrescriptionUpdateAPIView(
    # StaffEditorPermissionMixin,
    generics.UpdateAPIView
):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        # return super().perform_update(serializer)

prescription_update_view = PrescriptionUpdateAPIView.as_view()

class PrescriptionDestroyAPIView(
    # StaffEditorPermissionMixin,
    generics.DestroyAPIView
):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

prescription_destroy_view = PrescriptionDestroyAPIView.as_view()

class PrescriptionMixinView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # patient_name = serializer.validated_data.get('patient_name') or None
        doctor_name = serializer.validated_data.get('doctor_name') or None

        # if patient_name is None:
        #   raise ValidationError("Patient name is required")
        if doctor_name is None:
            doctor_name = "N/A"
        
        serializer.save()

prescription_mixin_view = PrescriptionMixinView.as_view()

# @api_view(['GET', 'POST'])
# def prescription_alt_view(request, pk=None, *args, **kwargs):
#   method = request.method

#   if method == "GET":
#     if pk is not None:
#       # detail view
#       object = get_object_or_404(Prescription, pk=pk) # obj
#       data = PrescriptionSerializer(object, many=False).data
#       return Response(data)
#     else:
#       # list view
#       queryset = Prescription.objects.all() # qs
#       data = PrescriptionSerializer(queryset, many=True).data
#       return Response(data)
  
#   if method == "POST":
#     serializer = PrescriptionSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#       patient_name = serializer.validated_data.get('patient_name')
#       doctor_name = serializer.validated_data.get('doctor_name')
#       issue_date = serializer.validated_data.get('issue_date')
#       expiry_date = serializer.validated_data.get('expiry_date')
#       return Response(serializer.data)
#     return Response({"message": "Invalid data"}, status=400)