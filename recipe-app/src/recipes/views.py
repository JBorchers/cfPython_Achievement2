from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import RecipeIngredientForm
from .models import Recipe


# Create your views here.

def add_ingredients(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)

    if request.method == 'POST':
        form = RecipeIngredientForm(request.POST)
        if form.is_valid():
            selected_ingredients = form.cleaned_data['ingredients']
            for ingredient in selected_ingredients:
                Recipe.objects.create(recipe=recipe, ingredient=ingredient)
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeIngredientForm()

    return render(request, 'recipes/add_ingredients.html', {'form': form, 'recipe': recipe})