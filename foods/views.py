from rest_framework.generics import ListAPIView

from foods.models import Food
from foods.serializers import FoodListSerializer


class ListFoodView(ListAPIView):
    queryset = Food.objects.filter(is_available=True)
    serializer_class = FoodListSerializer
