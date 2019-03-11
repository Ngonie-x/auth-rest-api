from rest_framework import serializers
from . import models

class HouseSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = models.HouseModel
        fields = ('id', 'house_owner', 'address', 'rent', 'house_pic','house_details', 'rooms', 'students', 'property_choice', 'gender', 'space_type', 'bathrooms', 'comments')


    def get_comments(self, obj):
        try:
            data = CommentSerializer(obj.comments.get(id=obj.id)).data
            return data
        except:
            data = None
            return data
        
    



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ('house', 'author', 'text')
