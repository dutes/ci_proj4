from django.shortcuts import render, redirect
from.models import Recipe
from recipe_share_app.forms import RecipeForm
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


# edit recipe page
def edit_recipe(request):
    recipies= Recipe.objects.all()
    return render(request, 'edit_recipe.html', {'recipies': recipies})

def edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    form = RecipeForm(request.POST, request.FILES, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe}) 

