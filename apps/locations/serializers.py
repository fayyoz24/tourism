from .models import (HistoricalLocation, Restaurant, 
                    Hotel, HistoricalLocationImage, 
                    RestaurantImage, HotelImage)

from rest_framework import serializers

class HistoricalLocationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalLocationImage
        fields = ['image', 'is_cover']

class HistoricalLocationSerializer(serializers.ModelSerializer):
    images = HistoricalLocationImageSerializer(many=True, read_only=True)       
    class Meta:
        model = HistoricalLocation
        fields = ['id', 'name', 'description', 'established_year', 
                  'location', 'longitude', 'latitude', 'images']

class RestaurantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = ['image', 'is_cover']

class RestaurantSerializer(serializers.ModelSerializer):
    images = RestaurantImageSerializer(many=True, read_only=True)       
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'image', 'description', 
                  'cuisine_type', 'location', 'longitude', 
                  'latitude', 'images']