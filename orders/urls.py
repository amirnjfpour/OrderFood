from django.urls import path

from orders.views import ChangeOrderItemView, SubmitOrderView, GetCurrentOrderView

urlpatterns = [
    path("order-item/", ChangeOrderItemView.as_view(), name="order_item"),
    path("submit-order/", SubmitOrderView.as_view(), name="submit_order"),
    path("current-order/", GetCurrentOrderView.as_view(), name="current_order"),
]
