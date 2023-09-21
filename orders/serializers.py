from rest_framework import serializers

from orders.models import OrderItem, Order


class BaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("user",)


class AddOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ("id", "count")


class OrderItemSerializer(serializers.ModelSerializer):
    item = serializers.CharField(source="item.name")

    class Meta:
        model = OrderItem
        fields = ("item", "count")


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        exclude = ("id", "user", "status")
