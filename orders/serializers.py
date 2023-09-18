from rest_framework import serializers

from orders.models import OrderItem, Order


class BaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("user", )


class AddOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ("id", "count")
