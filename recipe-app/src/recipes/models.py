from django.db import models
from django.shortcuts import reverse

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    cooking_time = models.PositiveIntegerField()
    description = models.TextField(default="N/A")
    difficulty = models.CharField(max_length=20, default="N/A")
    ingredients = models.ManyToManyField('ingredients.Ingredient', through='recipesingredients.RecipeIngredient', related_name='recipes')
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg') # default stored in src/media

    def calc_difficulty(self):
        num_ingredients = self.ingredients.count()

        if self.cooking_time < 10 and num_ingredients < 4:
            return "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            return "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            return "Intermediate"
        else:
            return "Hard"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.difficulty = self.calc_difficulty()
        super().save(update_fields=["difficulty"])



    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ("recipes:detail", kwargs={'pk': self.pk})