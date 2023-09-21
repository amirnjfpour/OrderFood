from django.urls import path

from foods.views import ListFoodView, RetrieveFoodView, ListCategoryView

urlpatterns = [
    path("", ListFoodView.as_view(), name="list_food"),
    path("categories/", ListCategoryView.as_view(), name="list_categories"),
    path("<pk>", RetrieveFoodView.as_view(), name="retrieve_food"),
]
