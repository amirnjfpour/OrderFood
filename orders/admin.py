from django.contrib import admin

from orders.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ["user", "created_at", "status", "overall_price"]
    list_filter = ["status", "user"]


admin.site.register(Order, OrderAdmin)
