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

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['name', 'price', "volume", 'is_available', "store"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['owner', 'price', "food", 'drink', "estimated_duration", "created_at", "status", "notes", "store"]