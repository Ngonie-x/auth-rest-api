from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone



class HouseModel(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    house_owner = models.CharField(max_length=265)
    address = models.CharField(max_length=255)
    rent = models.PositiveIntegerField()
    house_details = models.TextField()
    house_pic = models.ImageField(upload_to='houses', blank=True, null=True)
    
    rooms = models.PositiveIntegerField()
    students = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    ##
    gender_type = (('Female', 'Female'), ('Male', 'Male'), ('Both', 'Both'))
    gender = models.CharField(max_length=20, choices = gender_type, default = '0')
    ##
    property_type = (('Apartment', 'Apartment'),('Full House', 'Full House'), ('Rooms', 'Rooms'))
    property_choice = models.CharField(max_length=20, choices = property_type, default='2')
    ##
    student_gets = (('Shared Room', 'Shared Room'),('Private Room', 'Private Room'), ('Entire Space', 'Entire Space'))
    space_type = models.CharField(max_length=20, choices = student_gets, default = '0')
    ##
    



    def __str__(self):
        return self.address
    

class Review(models.Model):
    house = models.ForeignKey('HouseModel', related_name = 'comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.text