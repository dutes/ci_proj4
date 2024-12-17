from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Recipe
from .forms import RecipeForm
import re

def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "You need to login to access that page")
            return redirect('index')
        return view_func(request, *args, **kwargs)
    return wrapper


# Create your views here.
# home page
def index(request):
    # Instantiate forms with prefixes to avoid ID conflicts in the DOM
    login_form = AuthenticationForm(prefix='login')  
    signup_form = UserCreationForm(prefix='signup')  

    if request.method == "POST":
        # AJAX validation
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            signup_form = UserCreationForm(request.POST, prefix='signup')
            if signup_form.is_valid():
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': signup_form.errors.get_json_data()})
        
        # Handle Login Form
        if "login" in request.POST:
            login_form = AuthenticationForm(data=request.POST, prefix='login')
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                messages.success(request, "You have logged in successfully!")
                return redirect('index')
            else:
                messages.error(request, "Login failed, please check your username and password.")
                
        # Handle Signup Form
        elif "signup" in request.POST:
            signup_form = UserCreationForm(request.POST, prefix='signup')
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                return redirect('index')
            # Fallback for non-AJAX requests
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': signup_form.errors.get_json_data()})

    return render(request, 'index.html', {'login_form': login_form, 'signup_form': signup_form})

# logout view
def logout_view(request):
    logout(request)
    messages.success(request, "you have successfully logged out")
    return redirect('index')

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
@custom_login_required
def add_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form=RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            messages.success(request,
                f'Your recipe "{recipe.name}" has been added to the "{recipe.category}" page.')
            form=redirect('add_recipe')
    return render(request, 'add_recipe.html', {'form':form})

# delete recipe page
@custom_login_required
def delete(request):
    if request.method == 'POST':
        recipe_ids = request.POST.getlist("recipe_id")
        if recipe_ids:
            Recipe.objects.filter(id__in=recipe_ids).delete()
            messages.success(request, 'Selected recipe was deleted')
        return redirect('delete')
    
    recipes = Recipe.objects.all()
    return render(request, 'delete.html', {'recipes': recipes})

# get recipes for edit page
@custom_login_required
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
@custom_login_required
def edit_recipe(request):
    recipes = Recipe.objects.all()
    return render(request, 'edit_recipe.html', {'recipes': recipes})

# update recipe
@custom_login_required
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

#logout 
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('index')