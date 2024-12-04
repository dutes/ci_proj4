from django.shortcuts import render
from.models import Recipe
# Create your views here.
# home page
def index(request):
    return render(request, 'index.html')

# starters page
def starters(request):
    return render(request, 'starters.html')

# mains page
def mains(request):
    recipes = Recipe.objects.filter(category='Mains')
    return render(request, 'mains.html', {'recipes': recipes})

# deserts page
def desserts(request):
    return render(request, 'desserts.html')

# add recipe page
def add_recipe(request):
    return render(request, 'add_recipe.html')
