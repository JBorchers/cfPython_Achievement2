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


<details>
<summary><h2>Django MVT revisited</h2></summary>

### 1.	Update models if needed
   - I haven’t made any huge updates to my models. I still have three separate models: recipes, ingredients, and recipeingredients. Though I know there is a way to add the third model into one of the others, I found that the separation made things more organized and easier to manage.<br>
   - A simple update I had made was automating the calc_difficulty field based on number of ingredients and cooking time. Previously I had not had the functionality in place and values had to be manually entered. I also created an option to add a description to each recipe. Both the difficulty and description are required fields, but if no values are added, they are auto-populated with “no description” or “N/A”. <br>


### 2.	Adding records
   - Collect the information/media that will be added to the database.
   - Make entries in the Django admin panel for several recipes.

_Recipe Entries_

<img src="./Exercise_2.5/data_entries.png" width="50%"><img src="./Exercise_2.5/data_entries2.png" width="50%">

### 3.	Develop a welcome page
   - Take inspiration from existing applications. See [Learning Journal](https://github.com/JBorchers/cfPython_Achievement2/blob/main/Exercise_2.5/learning_journal_2.5.pdf)

_Welcome page for 2.5_

<img src="./Exercise_2.5/welcome.png" width="50%">


### 3.	Generate a recipes list

_Recipe App Sub-Page_

<img src="./Exercise_2.5/recipes-overview.png" width="50%">


### 5.	Add recipe details <br>

_Recipe 1 example_

<img src="./Exercise_2.5/recipe1.1.png" width="50%"><img src="./Exercise_2.5/recipe1.2.png" width="50%">

_Recipe 2 example_

<img src="./Exercise_2.5/recipe2.1.png" width="50%"><img src="./Exercise_2.5/recipe2.2.png" width="50%">


### 6.	Repeat if necessary


### 7.	Run tests

```
from django.test import TestCase
from .models import Recipe
from ingredients.models import Ingredient

class RecipeModelTestCase(TestCase):

    def setUp(self):
        # Set up test data
        self.ingredient = Ingredient.objects.create(name='Test Ingredient')
        self.recipe = Recipe.objects.create(
            name='Test Recipe',
            cooking_time=5,
            difficulty='Easy'
        )
        self.recipe.ingredients.add(self.ingredient)

    def test_recipe_has_ingredient(self):
        self.assertEqual(self.recipe.ingredients.count(), 1)
        self.assertEqual(self.recipe.ingredients.first(), self.ingredient)

    
    def test_get_absolute_url(self):
        self.recipe = Recipe.objects.create(
            name='Test Recipe',
            cooking_time=5,
            difficulty='Easy'
        )
        self.assertEqual(self.recipe.get_absolute_url(), "/list/2")
```

_Test Results:_ <br>
<img src="./Exercise_2.5/tests.png" width="50%">




</details>

<!--------------------------------------------------------------------------------------------------------------------------------------------->
<!--------------------------------------------------------------------------------------------------------------------------------------------->


<details>
<summary><h2>User Authentication in Django</h2></summary>

### 1. Provide authentication
- create a login view - ensure you have the correct imports
```
src/recipe_project/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    form = AuthenticationForm(request, request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("recipes:recipes_list")
        else:
            # Add an error message to the form
            form.add_error(None, "Invalid username or password. Please try again.")
    
    return render(request, "auth/login.html", {"form": form})

```
- creat a login template
  
`src/templates/auth/login.html`

<img src="./Exercise_2.6/login_template.png" width="50%">

  
- register a view and map URL

```
# /src/recipe_project/urls.py

from .views import login_view

urlpatterns = [
    path("login/", login_view, name="login"),
]
```

- add a "login" button on homepage that directs user to authentication form

```
# src/recipes/templates/recipes/recipes_home.html

<body>
    <div class="container">
        <p class="title">Welcome to Your Recipe Book</p>
        <a href="{% url 'login' %}" class="login-button">Login to start cookin'</a>
    </div>
</body>
```
<img src="./Exercise_2.6/login_homepage.png" width="50%">

- redirect user to "Recipes List" page after successful login

```
# src/recipe_project/views.py

if user is not None:
    login(request, user)
    messages.info(request, f"You are now logged in as {username}.")
    return redirect("recipes:recipes_list")

```


### 2. Protect views
- identify pages that should be protected via authentication (recipes list, recipe details)
- since these are class views, we will use `LoginRequiredMixin`

```
from django.contrib.auth.mixins import LoginRequiredMixin

class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipes_list.html"

class RecipesDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/details.html"
```
- user is now redirected to login page if either of these views are tried without prior authentication


### 3. Implement logout
- add logout button on each protected page

<img src="./Exercise_2.6/logout_button1.png" width="50%">

<img src="./Exercise_2.6/logout_button2.png" width="50%">

```
src/recipes/templates/recipes/recipes_list.html
src/recipes/templates/recipes/details.html

<a href="{% url 'logout' %}" class="logout-button">Logout</a>
```
  
- create a view for a successful logout (success.html)
- add a login button on the success.html page

```
src/recipe_project/urls.py

urlpatterns = [
    path(
        "success/",
        TemplateView.as_view(template_name="recipes/success.html"),
        name="success",
    ),
]
```

`src/recipes/templates/recipes/success.html`

<img src="./Exercise_2.6/logout_success.png" width="50%">


### 4. Run server 
- test user journey through the application

user enters homepage, clicks login button<br>
<img src="./Exercise_2.6/usr_journey/step1.png" width="50%">

user enters incorrect credentials<br>
<img src="./Exercise_2.6/usr_journey/step2_error.png" width="50%">

user enters correct credentials<br>
<img src="./Exercise_2.6/usr_journey/step2.png" width="50%">

user is directed to recipes list<br>
<img src="./Exercise_2.6/usr_journey/step3.png" width="50%">

user looks at specific recipe<br>
<img src="./Exercise_2.6/usr_journey/step4.png" width="50%">

user logs out<br>
<img src="./Exercise_2.6/usr_journey/step5.png" width="50%">

user can log back in<br>
<img src="./Exercise_2.6/usr_journey/step6.png" width="50%">




</details>

<!--------------------------------------------------------------------------------------------------------------------------------------------->
<!--------------------------------------------------------------------------------------------------------------------------------------------->


<details>
<summary><h2>Data Analysis and Visualization</h2></summary>

<h2> 1. Implement Search for Recipes </h2>

• Create a user form to allow your user to input the search criteria.
```
# src/recipes/forms.py

class RecipeSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        max_length=100,
        label="Search",
        widget=forms.TextInput(
            attrs={"class": "form-item", "placeholder": "Enter a Recipe Name or Ingredient"}
        ),
    )
    Ingredients = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Ingredient.objects.all(),
        label="Ingredient(s)",
        widget=forms.SelectMultiple(attrs={"class": "form-item"}),
    )
    selected_ingredient = forms.ModelChoiceField(
        required=False,
        queryset=Ingredient.objects.all(),
        label="Select Ingredient",
        empty_label="All Ingredients",
        widget=forms.Select(attrs={"class": "form-item"}),
    )
```

•	Extract the data as QuerySet using the search criteria.

```
# src/recipes/views.py

class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipes_list.html"
    context_object_name = "recipes"
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        recipe_name = self.request.GET.get("Recipe_Name")
        ingredients = self.request.GET.getlist("Ingredients")
        selected_ingredient = self.request.GET.get("selected_ingredient")

        if recipe_name:
            queryset = queryset.filter(name__icontains=recipe_name)

        if ingredients:
            ingredient_query = Q()
            for ingredient_id in ingredients:
                ingredient_query |= Q(ingredients__id=ingredient_id)
            queryset = queryset.filter(ingredient_query)

        # Include selected ingredient in the filter
        if selected_ingredient:
            queryset = queryset.filter(ingredients__id=selected_ingredient)

        return queryset
```
•	Convert the QuerySet to pandas DataFrames (Ensure you have pandas installed).
```
# src/recipes/views.py

class RecipesListView(LoginRequiredMixin, ListView):

  # previous code

  def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
  
          try:
              # Convert the QuerySet to a pandas DataFrame
              df = pd.DataFrame.from_records(context["recipes"].values())
              context["recipes_df"] = df
  
              context["form"] = RecipeSearchForm(self.request.GET)
```

•	Display search results as a table.
```
# src/recipes/views.py

class RecipesListView(LoginRequiredMixin, ListView):

  # previous code

  def generate_chart(request):
    chart_type = request.GET.get("chart_type")
    recipe_name = request.GET.get("Recipe_Name")
    ingredients = request.GET.getlist("Ingredients")

    # Filter the Recipe objects based on the request parameters
    queryset = Recipe.objects.all()

    if recipe_name:
        queryset = queryset.filter(name__icontains=recipe_name)

    if ingredients:
        for ingredient in ingredients:
            # Check if the ingredient parameter is empty
            if ingredient:
                queryset = queryset.filter(ingredients__id=ingredient)

    # Convert the filtered QuerySet to a list of dictionaries
    recipe_data = list(queryset.values())

    # Get the related Ingredient data for each recipe
    for data in recipe_data:
        recipe = Recipe.objects.get(pk=data["id"])
        data["ingredients"] = ", ".join(
            [ingredient.name for ingredient in recipe.ingredients.all()]
        )

    # Create the DataFrame from the list of dictionaries
    df = pd.DataFrame.from_records(recipe_data)

    chart_data = {"name": df["name"], "cooking_time": df["cooking_time"]}
    if chart_type == "#1":
        chart_data["labels"] = df["name"]
    elif chart_type == "#2":
        # For Pie Chart, labels should be the recipe names, and not the cooking times
        chart_data["labels"] = df["name"]
    else:
        chart_data["labels"] = None

    chart_image = get_chart(chart_type, chart_data)
    return JsonResponse({"chart_image": chart_image})
```
•	Ensure that the recipes returned by the search criteria are clickable and lead to the details page of the recipe.

```
# src/recipes/templates/recipes/recipe_list.html

 <!-- The list of recipes -->
    <div class="recipe-list">
        {% for object in object_list %}
        <div class="recipe-item">
            <a href="{{ object.get_absolute_url }}">
                <div class="recipe-title">{{ object.name }}</div>
                <img src="{{ object.pic.url }}" alt="{{ object.name }}" class="recipe-image">
            </a>
        </div>
        {% endfor %}
    </div>


# src/recipes/models.py

def get_absolute_url(self):
        return reverse ("recipes:detail", kwargs={'pk': self.pk})
```

<h2>2. Implement Show-All Function</h2>
Give users the ability to view all recipes without any search filter from the search criteria by clicking the "clear" button in the form. <br>
The clear function removes the user's selection and resets the recipe list to the original view with all recipes present.

```
# src/recipes/templates/recipes/recipes_list.html

<script>
        $(document).ready(function () {
            $("#clear-search").click(function () {
                // Clear the form fields
                $("#id_Recipe_Name").val("");
                $("#id_Ingredients").val([]).trigger("change");  // Clear the Ingredients field
                $("#id_chart_type").val("");  // Clear the chart_type field
                // Clear the chart by setting an empty src attribute
                $("#recipe-chart").attr("src", "");
                // Submit the form to refresh the recipe list
                $("form").submit();
            });
        });

    </script>
```

<h2>3. Data Visualization</h2>

1. Bar Chart (Horizontal Bar Chart):
    -X-axis: Recipe Name
    -Y-axis: Cooking Time

<img src="./Exercise_2.7/screenshots/bar_chart.png" width="50%"> 

3. Pie Chart:
    - Percentage of time it takes to cook each recipe in comparison to each other

<img src="./Exercise_2.7/screenshots/pie_chart.png" width="50%"> 

5. Line Chart:
    -X-axis: Recipe Name
    -Y-axis: Cooking Time

<img src="./Exercise_2.7/screenshots/line_chart.png" width="50%">


<h2>4. Write Tests</h2>

<img src="./Exercise_2.7/screenshots/tests.png" width="50%">

```
class RecipeSearchFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create some test data for the Recipe and Ingredient models
        ingredient1 = Ingredient.objects.create(name="Ingredient 1")
        ingredient2 = Ingredient.objects.create(name="Ingredient 2")
        recipe1 = Recipe.objects.create(id=1, name="Recipe 1", cooking_time=30)
        recipe2 = Recipe.objects.create(id=2, name="Recipe 2", cooking_time=60)
        recipe1.ingredients.add(ingredient1)
        recipe2.ingredients.add(ingredient2)

        # Create additional recipes
        for i in range(3, 13):  # Creates 10 additional recipes with ids 3 to 12
            recipe = Recipe.objects.create(
                id=i, name=f"Recipe {i}", cooking_time=(i + 1) * 10
            )
            recipe.ingredients.add(ingredient1)
            recipe.ingredients.add(ingredient2)

    def setUp(self):
        # Create a test user and log them in for the views requiring login
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_form_fields(self):
        form_data = {
            "Recipe_Name": "Recipe 1",
            "Ingredients": [1],
            "chart_type": "#1",
        }
        form = RecipeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_recipe_list_view(self):
        response = self.client.get("/recipes/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipes_list.html")

    def test_chart_generation(self):
        form_data = {
            "Recipe_Name": "",
            "Ingredients": [1],
            "chart_type": "#1",
        }
        response = self.client.get("/recipes/", form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("chart_image" in response.context)

    def test_view_protected(self):
        self.client.logout()
        response = self.client.get("/recipes/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/recipes/")

    def test_generate_chart_view(self):
        form_data = {
            "Recipe_Name": "",
            "Ingredients": [1],
            "chart_type": "#1",
        }
        response = self.client.get("/generate-chart/", form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("chart_image" in response.json())
```

<h2>5. Execution Flow</h2>



</details>

<!--------------------------------------------------------------------------------------------------------------------------------------------->
<!--------------------------------------------------------------------------------------------------------------------------------------------->
