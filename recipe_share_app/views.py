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
def delete_view(request):
    if request.method == 'POST':
        selected_recipes = request.POST.getlist("recipies_to_delete")
        Recipe.objects.filter(id__in=selected_recipes).delete()
        messages.success(request, 'Selected recipes have been deleted')
        return redirect('index')
    
    recipes = Recipe.objects.all()
    return render(request, 'delete_view.html', {'recipes': recipes})
