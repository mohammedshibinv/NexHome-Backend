from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Property
from .serializers import PropertyListSerializer, PropertyDetailsSerializer

class PropertiesListView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyListSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

class PropertyDetailsView(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailsSerializer
    permission_classes = []
    authentication_classes = [JWTAuthentication]
    lookup_field = 'pk'