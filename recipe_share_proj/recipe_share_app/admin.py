from django.contrib import admin
from .models import Recipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'date_created')
    search_fields = ['name', 'category']
    list_filter = ['category']
