from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # path for the landing page
    path('starters/', views.starters, name='starters'), # path for the starters page
    path('mains/', views.mains, name='mains'), # path for the mains page
    path('desserts/', views.desserts, name='desserts'), # path for the desserts page
    path('add_recipe/', views.add_recipe, name='add_recipe'), # path for the add recipe page
    path('delete_view/', views.delete_view, name='delete_view'), # path for the delete recipe page
]
