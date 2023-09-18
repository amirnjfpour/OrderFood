from django.urls import path

from orders.views import AddItemToOrder

urlpatterns = [
    path("add-item/", AddItemToOrder.as_view(), name="add_item_to_order"),
]
