from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from recipe_share_app.models import Recipe

class RecipeModelTest(TestCase):
    def test_recipe_creation(self):
        recipe=Recipe.objects.create(
            name="Test Recipe",
            ingredients="1 cup sugar, 2 cups of flour",
            instructions="Bang it all in a bowl and mix",
            category="Desserts"
    )
    self.assertEqual(recipe.name, "Test Recipe")
    self.assertEqual(recipe.category, "Desserts")
    self.assertsIsNotNone(recipe.date_created)
