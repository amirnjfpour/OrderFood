from django.contrib import admin

from foods.models import Category, Ingredient, Food

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Food)
