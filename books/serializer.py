from django.conf import settings
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model: Book
        fields = ['name', 'author', 'description']
    
    def validate_description(self, value):
        if len(value) > 300:
            raise serializers.ValidationError('The description is too long')
        return value

