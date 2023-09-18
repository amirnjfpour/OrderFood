from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import BaseUser
from foods.models import Food


class Order(models.Model):
    STATUSES = (("PRP", _("Preparing")),
                ("RDY", _("Ready")),
                ("RCV", _("Received")))
    user = models.ForeignKey(BaseUser, on_delete=models.RESTRICT, related_name="orders", verbose_name=_("user"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    modified_at = models.DateTimeField(auto_now=True, verbose_name=_("modified at"))
    status = models.CharField(max_length=10, choices=STATUSES, verbose_name=_("status"))
    overall_price = models.FloatField(verbose_name=_("overall price"))

    def __str__(self):
        return f"{self.user} - {self.created_at}"

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name=_("order"))
    item = models.ForeignKey(Food, on_delete=models.RESTRICT, related_name="order_items", verbose_name=_("item"))
    count = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)], verbose_name=_("count"))

    def __str__(self):
        return f"{self.order} - {self.item}"

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
