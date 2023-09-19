from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    cooking_time = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=20)
    ingredients = models.ManyToManyField('ingredients.Ingredient', through='recipesingredients.RecipeIngredient', related_name='recipes')
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg') # default stored in src/media
    
    def __str__(self):
        return self.name