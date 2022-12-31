from django.urls import path

from recipes.views import get_recipes_by_category, home

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('category/<int:category_id>', get_recipes_by_category, name='category')
]