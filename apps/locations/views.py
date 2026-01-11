from .models import HistoricalLocation, Restaurant, Hotel
from rest_framework.generics import ListAPIView
from .serializers import HistoricalLocationSerializer, RestaurantSerializer
# Create your views here.


class HistoricalLocationListView(ListAPIView):
    queryset = HistoricalLocation.objects.all()
    serializer_class = HistoricalLocationSerializer

class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# class HotelListView(ListAPIView):
#     queryset = Hotel.objects.all()
#     serializer_class = HotelSerializer