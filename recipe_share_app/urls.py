from django.urls import path
from django.contrib.auth import views as auth_views
from .views import logout_view
from . import views

urlpatterns = [
    path('', views.index, name='index'), # path for the landing page
    path('login/', auth_views.LoginView.as_view(template_name='custom_login.html'), name='login'), #view for login
    path('logout/', logout_view, name='logout'),
    path('starters/', views.starters, name='starters'), # path for the starters page
    path('mains/', views.mains, name='mains'), # path for the mains page
    path('desserts/', views.desserts, name='desserts'), # path for the desserts page
    path('add_recipe/', views.add_recipe, name='add_recipe'), # path for the add recipe page
    path('delete/', views.delete, name='delete'), # path for the delete recipe page
    path('edit_recipe/', views.edit_recipe, name='edit_recipe'),  # For listing recipes to edit
    path('edit_recipe/details/<int:recipe_id>/', views.recipe_details, name='recipe_details'),  # Fetch recipe details
    path('edit_recipe/update/<int:recipe_id>/', views.update_recipe, name='update_recipe'),  # Update recipe
]
