from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # path for the landing page
    path('starters/', views.starters, name='starters'), # path for the starters page
    path('mains/', views.mains, name='mains'), # path for the mains page
    path('desserts/', views.desserts, name='desserts'), # path for the desserts page
    path('add_recipe/', views.add_recipe, name='add_recipe'), # path for the add recipe page
    path('delete/', views.delete, name='delete'), # path for the delete recipe page
    path('edit_recipe/', views.edit_recipe, name='edit_recipe'), # path for the edit recipe page
]
