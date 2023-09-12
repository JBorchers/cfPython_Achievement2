# cfPython_Achievement2
 
<details>
<summary><h2>Creating the Recipe App with Django</h2></summary>
 
While the [previous achievement](https://github.com/JBorchers/cfPython_Achievement1/tree/main) built a command-line version of a recipe app, this achievement will redevelop the app using the Django framework.

Django is a high-level Python web framework that simplifies the process of building web applications by providing a set of tools and conventions for various web development tasks. It follows the Model-View-Controller (MVC) architectural pattern, which Django refers to as Model-View-Template (MVT):

- Models (M): In Django, models are Python classes that define the structure of your database tables. Each model class represents a table, and its attributes represent the columns of the table. Models define the data structure and can include fields, relationships, and methods for data manipulation.

- Views (V): Views handle the presentation logic and interact with the user. In the context of Django, views are Python functions or classes that process HTTP requests and return HTTP responses. They decide what data to display and how it should be displayed.

- Templates (T): Templates provide the HTML structure for your web pages. They separate the presentation layer from the logic in views. Django's template engine allows you to insert dynamic data into your HTML templates.

</details>

<!--------------------------------------------------------------------------------------------------------------------------------------------->
<!--------------------------------------------------------------------------------------------------------------------------------------------->


<details>
<summary><h2>Backend Project Set Up</h2></summary>

## MODELS

Here we are working with the **M** part of Django's **MVT** architecture.
The app is composed of four main entities:

- `Users`
- `Recipes`
- `Ingredients`
- `RecipesIngredients`

_Users_ :<br>This app handles user authentication, registration, login, and profile management.<br><br>
_Recipes_ :<br>Each recipe is listed for the user, displaying recipe name, cooking time, level of difficulty, and ingredients.<br><br>
_Ingredients_ :<br>All ingredients are stored in this app amongst all recipes.<br><br>
_RecipesIngredients_ :<br>This app handles the many-to-many relationship between recipes and ingredients. This is where ingredients are added to a selected recipe to then be appended to the recipe itself and stored in the `ingredients` app.<br><br>



</details>

<!--------------------------------------------------------------------------------------------------------------------------------------------->
<!--------------------------------------------------------------------------------------------------------------------------------------------->


<details>
<summary><h2>Django Project Views and Templates</h2></summary>

In a Django project, "views" and "templates" are fundamental components that work together to handle the presentation logic and rendering of web pages. They are key elements of the Model-View-Controller (MVC) architectural pattern used in Django.

Views handle the application logic and process requests, while templates define the structure and presentation of the resulting web pages. Together, they enable Django to build dynamic and data-driven web applications.

The front-end of the **Recipes** application will be build using these views and templates.

### Create a `View`

Create a `view.py` file under the desired app. Specify a `recipes_home.html` template, that you will create in the next step. Be sure to include the proper imports.

```
# src > recipes > views.py
from django.shortcuts import render

# Create your views here.
def recipes_home(request):
    return render(request, "recipes/recipes_home.html")
```

### Create a `Template`

Create a `templates` folder under the same app (`recipes`) as the `views.py`. <br>
Create another folder of the same name, `recipes`. <br>
Create an HTML file to define the main page template. Call it `recipes_home.html`.
Design welcome page and save it. <br>

```
# src > recipes > templates > recipes_home.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Recipes</title>
    <style>
      body {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
      }
    </style>
  </head>
  <body>
    <h1>Welcome to your personalized Recipes App!</h1>
    <h3>Let's get cookin!</h3>
    <ul>
      {% for recipe in recipes %}
      <li>
        <a href="/recipes/{{ recipe.id }}">{{ recipe.title }}</a>
      </li>
      {% endfor %}
    </ul>
    <a href="/recipes/new">Add a new recipe</a>
  </body>
</html>
```

### Map view to URL

In order for the welcome page to appear when the site is first loaded, map the template to a `urls.py` file under the `recipes` app. <br>
Specify the `path` to connect the route corresponding to “http://127.0.0.1:8000/” with the view specified by `recipes/views.py`. <br>
Ensure the proper packages are imported.

```
# src > recipes > urls.py
from django.urls import path
from .views import recipes_home

app_name = "recipes"

urlpatterns = [
    path("", recipes_home, name="recipes_home"),
]
```

Next, register the view to the `urlpatterns` in the main project folder's `urls.py`.
```
# src > recipe_project > urls.py
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("recipes.urls"))
]
```

### Run server

In the terminal, activate your virtual environment. Run the server by typing `python manage.py runserver`

### Load site in browser

Copy the link provided by running the server and paste it into the browser. The custom webpage should now be loaded.


</details>

<!--------------------------------------------------------------------------------------------------------------------------------------------->
<!--------------------------------------------------------------------------------------------------------------------------------------------->
