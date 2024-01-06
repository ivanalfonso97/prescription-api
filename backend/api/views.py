from rest_framework.response import Response
from rest_framework.decorators import api_view

from prescriptions.serializers import PrescriptionSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = PrescriptionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({"message": "Invalid data"}, status=400)