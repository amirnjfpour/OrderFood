from django_filters import FilterSet

from foods.models import Food


class FoodFilter(FilterSet):
    class Meta:
        model = Food
        fields = {
            "category": ["exact"]
        }
