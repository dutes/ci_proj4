from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True)
    ingredients = models.TextField(max_length=1000)
    instructions = models.TextField(max_length=5000)
    category = models.CharField(
    max_length=50,
    choices=[('Starters', 'Starters'), ('Mains', 'Mains'), ('Desserts', 'Desserts')]
    )
    image = models.ImageField(upload_to='images/', null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name