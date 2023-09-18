from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAuthenticated
from orders.models import Order, OrderItem
from orders.serializers import AddOrderItemSerializer, BaseOrderSerializer


class AddItemToOrder(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        mutable_data = request.data.copy()
        if Order.objects.filter(user=user, status="IPR").exists():
            order = Order.objects.filter(user=user, status="IPR").first()
        else:
            order_serializer = BaseOrderSerializer(data={"user": user.id})
            order_serializer.is_valid(raise_exception=True)
            order_serializer.save()
            order = order_serializer.instance
        mutable_data["order"] = order.id
        if OrderItem.objects.filter(order=order, item=mutable_data["item"]).exists():
            order_item = OrderItem.objects.filter(order=order, item=mutable_data["item"]).first()
            order_item.count += 1
            order_item.save()
        else:
            item_serializer = AddOrderItemSerializer(data=mutable_data)
            item_serializer.is_valid(raise_exception=True)
            item_serializer.save()
            order_item = item_serializer.instance
        added_price = order_item.item.price * order_item.count
        order.overall_price += added_price
        order.save()
        return Response({"message": "done"}, status=status.HTTP_200_OK)
