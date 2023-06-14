from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
import re


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = user_profile
        fields = '__all__'

    def validate_email(self, value):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.match(email_regex,value):
            raise serializers.ValidationError('Email must be from example.com domain.')
        return value