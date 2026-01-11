from django.db import models

# Create your models here.

class HistoricalLocation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    established_year = models.IntegerField()
    location = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name

class HistoricalLocationImage(models.Model):
    location = models.ForeignKey(HistoricalLocation, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='locations/')
    is_cover = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.location.name}"

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='locations/')
    description = models.TextField()
    cuisine_type = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name

class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='locations/')
    is_cover = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.restaurant.name}"

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    star_rating = models.IntegerField()
    location = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='locations/')
    is_cover = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.hotel.name}"