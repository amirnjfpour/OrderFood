from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name=_("name"))
    photo = models.ImageField(verbose_name=_("photo"))
    photo_alt_text = models.CharField(max_length=50, verbose_name=_("photo alt text"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Ingredient(models.Model):
    name = models.CharField(max_length=40, verbose_name=_("name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Ingredient")
        verbose_name_plural = _("Ingredients")


class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name="foods", verbose_name=_("category"))
    name = models.CharField(max_length=40, verbose_name=_("food"))
    ingredients = models.ManyToManyField(Ingredient, related_name="foods", verbose_name=_("ingredients"))
    price = models.FloatField(verbose_name=_("price"))
    photo = models.ImageField(verbose_name=_("photo"))
    photo_alt_text = models.CharField(max_length=50, verbose_name=_("photo alt text"))
    is_available = models.BooleanField(default=True, verbose_name=_("is available"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Food")
        verbose_name_plural = _("Foods")
