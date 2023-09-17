from rest_framework import serializers

from foods.models import Food, FoodIngredient


class FoodListSerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField()

    class Meta:
        model = Food
        exclude = ("category", "is_available",)

    @staticmethod
    def get_ingredients(obj: Food):
        ingredient_objects = FoodIngredient.objects.filter(food=obj)
        ingredients = []
        for ingredient_object in ingredient_objects:
            if ingredient_object.amount is None:
                ingredients.append(ingredient_object.ingredient.name)
            else:
                ingredients.append(f"{ingredient_object.amount} {ingredient_object.ingredient.name}")
        return ingredients
