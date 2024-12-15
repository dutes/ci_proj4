from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image

# Create your tests here.
from recipe_share_app.models import Recipe
from recipe_share_app.forms import RecipeForm

# =======================
# Helper method for tests
# to generate iamge files
#========================
class ImgTestHelper:
    @staticmethod
    def generate_image_file():
        """
        Generate a simple image file for testing purposes.
        """
        img=BytesIO()
        img_obj=Image.new("RGB", (100, 100), color="red") #create a red image file 100x100px
        img_obj.save(img, format='JPEG') # save as jpeg
        img.seek(0) #reset file pointer
        return SimpleUploadedFile('test_image.jpg', img.read(), content_type="image/jpeg")

# =======================
# Model tests
#========================
class RecipeModelTest(TestCase):
    """
    Tests related to recipe model functionality
    """

    def test_recipe_creation(self):
        """
        Verify a recipe can be created succcessfully
        """
        recipe=Recipe.objects.create(
            name="test recipe",
            ingredients="1 cup water, 2 cups sugar",
            instructions="bang it all in a bowl and mix",
            category="Desserts"
        )
        self.assertEqual(recipe.name, "test recipe")
        self.assertEqual(recipe.category, "Desserts")
        self.assertIsNotNone(recipe.date_created)

    def test_str_method(self):
        """
        Verify the __str__ method returns the recipe name.
        """
        recipe = Recipe.objects.create(
            name="test recipe",
            ingredients="1 cup water, 2 cups sugar",
            instructions="bang it all in a bowl and mix",
            category="Desserts"
        )
        self.assertEqual(str(recipe), "test recipe")
    
    def test_date_created_auto_populated(self):
        """
        Verify the date_created field is automatically populated.
        """
        recipe = Recipe.objects.create(
            name="test recipe",
            ingredients="1 cup water, 2 cups sugar",
            instructions="bang it all in a bowl and mix",
            category="Desserts"
        )
        self.assertIsNotNone(recipe.date_created)

    def test_recipe_deletion(self):
        """
        verify that recipes can be deleted
        """
        recipe = Recipe.objects.create(
            name="test recipe",
            ingredients="1 cup water, 2 cups sugar",
            instructions="bang it all in a bowl and mix",
            category="Desserts"
        )
        self.assertEqual(Recipe.objects.count(), 1)
        recipe.delete()
        self.assertAlmostEqual(Recipe.objects.count(), 0)
        

# =======================
# Form tests
#========================
class RecipeFormTest(TestCase):
    """
    Tests related to form validation and functionality
    """

    def test_valid_recipe_form(self):
        """
        verify that a valid form passes validation
        """
        form_data = {
            'name': 'pasta',
            'ingredients': 'pasta, tomato sauce',
            'instructions': 'boil and sauce',
            'category': 'Mains'
        }
        file_data = {
            'image': ImgTestHelper.generate_image_file()
        }
        form = RecipeForm(data=form_data, files=file_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_recipe_form_missing_required_fields(self):
        """
        Verify that the form fails validation if required fields are missing.
        """
        form_data = {
            'name': '',
            'ingredients': 'pasta, tomato sauce',
            'instructions': 'boil and sauce',
            'category': 'Mains'
        }
        file_data = {
            'image': ImgTestHelper.generate_image_file()
        }
        form = RecipeForm(data=form_data, files=file_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
    
    def test_missing_image_field(self):
        """
        Verify that the form fails validation if the image field is missing.
        """
        form_data = {
            'name': 'pasta',
            'ingredients': 'pasta, tomato sauce',
            'instructions': 'boil and sauce',
            'category': 'Mains'
        }
        form = RecipeForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors)
    
    def test_invalid_category(self):
        """
        verify that an invalid category will fail validation 
        """
        form_data = {
            'name': 'soup',
            'ingredients': 'carrots, onion, cheese',
            'instructions': 'boild and blend',
            'category': 'Invalid' #something that will break
        }
        file_data = {
            'image':ImgTestHelper.generate_image_file()
        }
        form=RecipeForm(data=form_data, files=file_data)
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors)

    def test_recipe_form_no_image(self):
        """
        verify that form is invalid without image
        """
        form_data = {
            'name': 'pasta',
            'ingredients': 'pasta, tomato sauce',
            'instructions': 'boil and sauce',
            'category': 'Mains'
        }
        form = RecipeForm(data=form_data)#no files, no image
        self.assertFalse(form.is_valid())


# =======================
# edge case tests
#========================
class RecipeEdgeCases(TestCase):
    """
    Test for edge cases
    """

    def test_large_inputs(self):
        """
        verify large inputs amounts
        """
        form_data = {
            'name': 'A' * 200,
            'ingredients': 'B' * 500,
            'instructions': 'C' * 1000,
            'category': 'Mains'
        }
        file_data = {
            'image': ImgTestHelper.generate_image_file()
        }
        form = RecipeForm(data=form_data, files=file_data)
        self.assertTrue(form.is_valid())

    def test_greater_than_allowed_input(self):
        """
        verify that user can't input more than the allowed chars
        """
        form_data = {
            'name': 'A' * 2000,
            'ingredients': 'B' * 1500,
            'instructions': 'C' * 11000,
            'category': 'Mains'
        }
        file_data = {
            'image': ImgTestHelper.generate_image_file()
        }
        form = RecipeForm(data=form_data, files=file_data)
        self.assertFalse(form.is_valid())

    def test_invalid_image_file(self):
        """
        test that invalid file types are not allowed for image
        """
        form_data = {
            'name': 'soup',
            'ingredients': 'carrots, onion, cheese',
            'instructions': 'boild and blend',
            'category': 'Desserts'
        }
        file_data = {
            'iamge': SimpleUploadedFile("test.txt", b"not an image", content_type="text/plain")
        }
        form = RecipeForm(data=form_data, files=file_data)
        self.assertFalse(form.is_valid())
        self.assertIn('image',form.errors)

    def test_sql_injection_attempt(self):
        """
        just making sure SQL injection isn't going to work
        """
        form_data = {
            'name': 'pasta"; DROP TABLE Recipe;--',
            'ingredients': 'pesto, cheese, garlic',
            'instructions': 'boil and slop',
            'category': 'Mains'
        }
        file_data = {
            'image': ImgTestHelper.generate_image_file()
        }
        form = RecipeForm(data=form_data, files=file_data)
        if form.is_valid():
            recipe=form.save()
            self.assertEqual(recipe.name, 'pasta"; DROP TABLE Recipe;--' )
            self.assertEqual(Recipe.objects.count(), 1)

    def test_non_ascii_chars(self):
        """
        verify that recipes can include non ASCII chars
        """
        recipe = Recipe.objects.create(
            name="Crème Brûlée",
            ingredients="2 cups crème, 1 tsp brûlée sugar",
            instructions="Mix and bake",
            category="Desserts"
        )
        self.assertEqual(recipe.name,"Crème Brûlée")

    def test_duplicate_recipe(self):
        """
        verify that a duplicate recipe cannot be created
        """
        Recipe.objects.create(
          name="Test Recipe",
            ingredients="1 cup sugar, 2 cups flour",
            instructions="Mix and bake",
            category="Desserts"  
        )
        duplicate_recipe = Recipe(
            name="Test Recipe",
            ingredients="1 cup sugar, 2 cups flour",
            instructions="Mix and bake",
            category="Desserts"
        )
        with self.assertRaises(Exception):
            duplicate_recipe.save()
















