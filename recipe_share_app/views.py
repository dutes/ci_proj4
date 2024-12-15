from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Recipe
from .forms import RecipeForm

# Create your views here.
# home page
def index(request):
    return render(request, 'index.html')

# starters page
def starters(request):
    recipes = Recipe.objects.filter(category='Starters')
    return render(request, 'starters.html', {'recipes': recipes})

# mains page
def mains(request):
    recipes = Recipe.objects.filter(category='Mains')
    return render(request, 'mains.html', {'recipes': recipes})

# deserts page
def desserts(request):
    recipes = Recipe.objects.filter(category='Desserts')
    return render(request, 'desserts.html', {'recipes': recipes})

# add recipe page
def add_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form=RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            messages.success(
                request,
                f'Your recipe "{recipe.name}" has been added to the "{recipe.category}" page.'
            )
            form=RecipeForm()
    return render(request, 'add_recipe.html', {'form':form})

# delete recipe page
def delete(request):
    if request.method == 'POST':
        recipe_ids = request.POST.getlist("recipe_id")
        if recipe_ids:
            Recipe.objects.filter(id__in=recipe_ids).delete()
            messages.success(request, 'Selected recipe was deleted')
        return redirect('index')
    
    recipes = Recipe.objects.all()
    return render(request, 'delete.html', {'recipes': recipes})

# get recipes for edit page
def recipe_details(request, recipe_id):
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        data = {
            "name": recipe.name,
            "ingredients": recipe.ingredients,
            "instructions": recipe.instructions,
            "category": recipe.category,
            "image": recipe.image.url if recipe.image else "",
        }
        return JsonResponse(data)

# edit recipe page
def edit_recipe(request):
    recipes = Recipe.objects.all()
    return render(request, 'edit_recipe.html', {'recipes': recipes})

# update recipe
def update_recipe(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Recipe updated successfully'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=405)
