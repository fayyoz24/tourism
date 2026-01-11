from .views import (HistoricalLocationListView, 
                    RestaurantListView,) #HotelListView
from django.urls import path


app_name = 'locations'

urlpatterns = [
    path('historical-locations/', HistoricalLocationListView.as_view(), name='historical_locations'),
    path('restaurants/', RestaurantListView.as_view(), name='restaurants'),
    # path('hotels/', HotelListView.as_view(), name='hotels'),

]