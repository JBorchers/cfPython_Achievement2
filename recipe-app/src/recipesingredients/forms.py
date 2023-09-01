from django import forms
from .models import Ingredient

class RecipeIngredientForm(forms.Form):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )