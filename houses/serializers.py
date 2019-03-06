from rest_framework import serializers
from . import models

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HouseModel
        fields = ('id', 'house_owner', 'address', 'rent', 'house_pic','house_details', 'rooms', 'students', 'property_choice', 'gender', 'space_type', 'bathrooms')