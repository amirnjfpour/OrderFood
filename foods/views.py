from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from foods.filters import FoodFilter
from foods.models import Food
from foods.serializers import FoodListSerializer


class ListFoodView(ListAPIView):
    queryset = Food.objects.filter(is_available=True)
    serializer_class = FoodListSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["name", "category__name"]
    ordering_fields = ["price"]
    filterset_class = FoodFilter
