from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(
    max_length=50,
    choices=[('Starters', 'Starters'), ('Mains', 'Mains'), ('Desserts', 'Desserts')]
    )
    image = models.ImageField(upload_to='images/', null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name