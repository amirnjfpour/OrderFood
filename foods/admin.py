from django.contrib import admin

from foods.models import Category, Ingredient, Food, FoodIngredient

admin.site.register(Category)
admin.site.register(Ingredient)


class FoodIngredientInline(admin.TabularInline):
    model = FoodIngredient


class FoodAdmin(admin.ModelAdmin):
    inlines = [FoodIngredientInline]


admin.site.register(Food, FoodAdmin)
