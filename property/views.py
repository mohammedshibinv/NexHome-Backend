from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from .models import Property
from .serializers import PropertyListSerializer

@api_view(['GET'])
@authentication_classes([])  # If public access is intentional
@permission_classes([])      # If public access is intentional
def properties_list(request):
    properties = Property.objects.all()
    serializer = PropertyListSerializer(properties, many=True)
    return Response({"data": serializer.data})
