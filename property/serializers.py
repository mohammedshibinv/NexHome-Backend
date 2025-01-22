from rest_framework import serializers
from .models import Property
from useraccount.serializers import UserDetailsSerializer

class PropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = {"property_id","title","price_per_night","image_url"}

class PropertyDetailsSerializer(serializers.ModelSerializer):
    landlord = UserDetailsSerializer(read_only=True,many=False)
    class Meta:
        model = Property
        fields = {"property_id","title","description","price_per_night","image_url","category","landlord"}
