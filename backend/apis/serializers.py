from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.settings import api_settings
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
    

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=courses
        fields='__all__'

class universitycourseSerializer(serializers.ModelSerializer):

    course_offered=CoursesSerializer(read_only=True, many=True)
    class Meta:
        model=course_offer_university
        fields=('university_name','course_offered')
class coursebooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=books
        fields='__all__'


class CustomSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=books
        fields='__all__'

