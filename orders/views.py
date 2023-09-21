from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAuthenticated
from orders.models import Order, OrderItem
from orders.serializers import AddOrderItemSerializer, BaseOrderSerializer, OrderSerializer


class ChangeOrderItemView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        data = request.data
        try:
            adjunct = int(data.get("adjunct"))
        except:
            return Response({"error": "invalid adjunct"}, status=status.HTTP_400_BAD_REQUEST)
        if not (adjunct == 1 or adjunct == -1):
            return Response({"error": "invalid adjunct"}, status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        if Order.objects.filter(user=user, status="IPR").exists():
            order = Order.objects.filter(user=user, status="IPR").first()
        else:
            order_serializer = BaseOrderSerializer(data={"user": user.id})
            order_serializer.is_valid(raise_exception=True)
            order_serializer.save()
            order = order_serializer.instance
        mutable_data = data.copy()
        mutable_data["order"] = order.id
        if OrderItem.objects.filter(order=order, item=mutable_data["item"]).exists():
            order_item = OrderItem.objects.filter(order=order, item=mutable_data["item"]).first()
            if order_item.count == 1 and adjunct == -1:
                order_item.delete()
                return Response({"message": "done"}, status=status.HTTP_200_OK)
            else:
                order_item.count += adjunct
                order_item.save()
        else:
            if adjunct == -1:
                return Response({"error": "invalid action"}, status=status.HTTP_400_BAD_REQUEST)
            item_serializer = AddOrderItemSerializer(data=mutable_data)
            item_serializer.is_valid(raise_exception=True)
            item_serializer.save()
            order_item = item_serializer.instance
        added_price = order_item.item.price * adjunct
        order.overall_price += added_price
        order.save()
        return Response({"message": "done"}, status=status.HTTP_200_OK)


class SubmitOrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request):
        user = request.user
        if not Order.objects.filter(user=user, status="IPR").exists():
            return Response({"message": "you don't have any in progress order"}, status=status.HTTP_400_BAD_REQUEST)
        order = Order.objects.filter(user=user, status="IPR").first()
        order.status = "PRP"
        order.save()
        return Response({"message": "done"}, status=status.HTTP_200_OK)


class GetCurrentOrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        if not Order.objects.filter(user=user, status="IPR").exists():
            return Response({"message": "you don't have any in progress order"}, status=status.HTTP_400_BAD_REQUEST)
        order = Order.objects.filter(user=user, status="IPR").first()
        serializer = OrderSerializer(order)
        return Response(serializer.data)
