import uuid
from django.db import models

from useraccount.models import User

# Create your models here.
class Property(models.Model):
    property_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    titile = models.CharField(max_length=32)
    description = models.TextField()
    price_per_night = models.IntegerField()
    bedrooms = models.IntegerField()
    guests = models.IntegerField()
    country = models.CharField(max_length=48)
    country_code = models.CharField(max_length=10)
    category = models.CharField(max_length=255)
    #favorited
    image = models.ImageField(max_length=255)
    landlord = models.ForeignKey(User, related_name='properties', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)