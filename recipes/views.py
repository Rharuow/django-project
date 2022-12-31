from django.shortcuts import render

from .models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.all()

    return render(request, 'recipes/home.html', context={
        'recipes': recipes
    })


def get_recipes_by_category(request, category_id):

    recipes_by_category = Recipe.objects.filter(category__id=category_id)

    return render(request, 'recipes/recipes_by_category.html', context={
        'recipes_by_category': recipes_by_category
    })
