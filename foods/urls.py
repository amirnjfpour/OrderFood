from django.urls import path

from foods.views import ListFoodView, RetrieveFoodView

urlpatterns = [
    path("", ListFoodView.as_view(), name="list_food"),
    path("<pk>", RetrieveFoodView.as_view(), name="retrieve_food"),
]
