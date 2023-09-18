from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import BaseUser
from foods.models import Food


class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="comments", verbose_name=_("food"))
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name="comments", verbose_name=_("user"))
    text = models.TextField(verbose_name=_("text"))
    score = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],
                                        verbose_name=_("score"))
    public_name = models.CharField(max_length=20, verbose_name=_("public name"))

    def __str__(self):
        return f"{self.user} - {self.food}"

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
