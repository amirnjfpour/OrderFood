from django.urls import path

from orders.views import AddItemToOrder, SubmitOrderView

urlpatterns = [
    path("add-item/", AddItemToOrder.as_view(), name="add_item_to_order"),
    path("submit-order/", SubmitOrderView.as_view(), name="submit_order"),
]
