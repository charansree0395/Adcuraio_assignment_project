from application.models import *
from rest_framework import serializers 

class UserForm(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username','password','email']
        


class FoodForm(serializers.ModelSerializer):
    class Meta:
        model = Food_blog
        fields = '__all__'
