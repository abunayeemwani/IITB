from django.contrib.auth.models import User
from .models import Card, Column

from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class CardSerializer(serializers.ModelSerializer):
    def validate_title(self, title):
        if not title.isalpha():
            raise serializers.ValidationError('Title should contain only alphabets!')
        return title

    def validate_description(self, description):
        if len(description) < 25:
            raise serializers.ValidationError('Description should be at least 25 characters long!')
        return description

    class Meta:
        model = Card
        fields = ['id', 'title', 'description', 'column', 'modified_at', 'author']

class ColumnSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)
    class Meta:
        model = Column
        fields = ['id', 'name', 'cards']