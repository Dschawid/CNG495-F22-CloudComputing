from rest_framework import serializers
from food.models import *

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'price', 'size', 'is_available', 'duration', 'category', 'store']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['name', 'location', 'owner']