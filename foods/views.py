from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from foods.filters import FoodFilter
from foods.models import Food, Category
from foods.serializers import FoodListSerializer, RetrieveFoodSerializer, CategorySerializer


class ListCategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListFoodView(ListAPIView):
    queryset = Food.objects.filter(is_available=True)
    serializer_class = FoodListSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["name", "category__name"]
    ordering_fields = ["price"]
    filterset_class = FoodFilter


class RetrieveFoodView(RetrieveAPIView):
    queryset = Food.objects.filter(is_available=True)
    serializer_class = RetrieveFoodSerializer
    lookup_field = "pk"
