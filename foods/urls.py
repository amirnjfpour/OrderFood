from django.urls import path

from foods.views import ListFoodView

urlpatterns = [
    path("", ListFoodView.as_view(), name="list_food"),
]
