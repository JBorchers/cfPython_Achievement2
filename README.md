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

The front-end of the `Recipes` application will be build using these views and templates.








</details>

<!--------------------------------------------------------------------------------------------------------------------------------------------->
<!--------------------------------------------------------------------------------------------------------------------------------------------->
