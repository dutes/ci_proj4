from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image

# Create your tests here.
from recipe_share_app.models import Recipe
from recipe_share_app.forms import RecipeForm

#add recipe is working
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
        self.assertIsNotNone(recipe.date_created)
#test to validate form validation
class RecipeFormTest(TestCase):
    def generate_image_file(self):
        img=BytesIO()
        img_obj=Image.new("RGB", (100, 100), color="red")
        img_obj.save(img, format='JPEG')
        img.seek(0)
        return SimpleUploadedFile('test_image.jpg', img.read(), content_type="image/jpeg")

    def test_valid_recipe_form(self):
        form_data = {
            'name': 'Pasta',
            'ingredients': 'Pasta, tomato sauce',
            'instructions': 'boil and sauce',
            'category': 'Mains'
        }
        file_data = {
            'image':self.generate_image_file()
        }
        form=RecipeForm(data=form_data, files=file_data)
        print (form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_recipe_form(self):
        form_data = {
            'name': '',
            'ingredients': 'garlic, pesto',
            'instructions': 'cook and slop',
            'category': 'starters'
                }
        file_data = {
            'image':self.generate_image_file()
        }
        form=RecipeForm(data=form_data, files=file_data)
        self.assertFalse(form.is_valid())
