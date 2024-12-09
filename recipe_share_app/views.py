from django.shortcuts import render, redirect
from.models import Recipe
from recipe_share_app.forms import RecipeForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

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
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm()
    print("this is the for, ", form)#debugging
    return render(request, 'add_recipe.html', {'form': form})

# delete recipe page
def delete(request):
    if request.method == 'POST':
        recipe_ids = request.POST.getlist("recipe_id")
        if recipe_ids:
            Recipe.objects.filter(id__in=recipe_ids).delete()
            messages.success(request, 'Selected recipes have been deleted')
        return redirect('index')
    
    recipes = Recipe.objects.all()
    return render(request, 'delete.html', {'recipes': recipes})

# recipe details page for editing
def recipe_details(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
        data= {
            "name": recipe.name,
            "ingredients": recipe.ingredients, 
            "instructions": recipe.instructions,
            "category": recipe.category,
        }
        return JsonResponse(data)
    except Recipe.DoesNotExist:
        return JsonResponse({"error": "Recipe not found."}, status=404)

# edit recipe 
def edit_recipe(request):
    recipes = Recipe.objects.all()  # Fix typo
    return render(request, 'edit_recipe.html', {'recipes': recipes})

# update recipe page
def edit(request, recipe_id):
    # Fetch the recipe or return a 404 error if not found
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        # Handle form submission
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('edit_recipe')  # Redirect to the edit page
    else:
        # For GET requests, return recipe details
        form = RecipeForm(instance=recipe)

    return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe})

