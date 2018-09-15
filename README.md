# Django-For-Beginners
A project-based approach to learning web development with the Django web framework

## Step 0: Installation
With pip in tow, we’ll install the following dependencies:
+ Django
+ Requests

To do so, simple run the following commands in your terminal:
```sh
$ pip install django
$ pip install requests
```
With that all said and done, let’s get into the development of the application.

## Step 1: Starting our project
To kick things off, let’s create our Django project. Within your terminal:
```sh
$ django-admin startproject demonstration
```
Let’s take a look at our brand new project:
+ manage.py: A command-line program allowing users to interact with their Django applications.
+ demonstration/init.py: An empty file signifying that this directory is considered a Python package.
+ demonstration/settings.py: A file consisting of key-value pairs for configuring your Django application.Here we can configure your databases, setup paths to static files, and much more.
+ demonstration/urls.py: Allows us to map view functions to [URLs](https://docs.djangoproject.com/en/1.8/topics/http/urls/), which is essentially a table of contents for our application.
+ demonstration/wsgi.py: Allows us to deploy [WSGI](https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/)-compatible web servers.

**Running the server**
```sh
$ python manage.py runserver
```
When running this command, you’ll be greeted with the following error in your terminal:
```bash
Performing system checks...

System check identified no issues (0 silenced).

You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 11, 2018 - 21:55:45
Django version 2.1.1, using settings 'demonstation.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Let’s go ahead and fix that. You can stop the server using Ctrl + C. Go ahead and run the following command:
```sh
$ python manage.py migrate
```
This command will build all of the default database tables that Django needs for built-in services such as user authentication. Once again, we’ll run the server, then navigate to http://127.0.0.1:8000/. Now it worked!

## Step 2: Creating our application
```sh
$ python manage.py startapp app
```
Breaking down these files:
+ app/admin.py: Allows us to register our models to view on the Django Admin Site.
+ app/migrations: Keeps track of our migrations which are essentially Django’s way of propagating changes that are made to our models.
+ app/models.py: Stores our representations of objects which will be stored in our database.
+ app/tests.py: Our unit tests will live here. Although Django calls these tests “unit tests”, they’re actually closer to integration tests.
+ app/views.py: All of our views will live here, which are mapped to URLs.

With that, we’ve successfully generated our project scaffold. Before moving on, we’ll configure our Settings.py while which will be important going forward.

**Configuring Settings.py**
Settings.py contains various configuration options available, such as changing our database and so much more. For this project, we’ll need to add the following lines anywhere in this file:
```
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
```
This will configure our paths for our Static files (CSS, JavaScript, images, etc) as well as the path to our template files. 
Lastly, we’ll need to register your application (named 'app') under the INSTALLED_APPS section.

We’ll now move onto configuring a basic URL.

## Step 3: First View
As mentioned earlier, URLs map to functions in your views.py which in turn will pass data to a template. Within app/views.py:
```python
# views.py
from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

# ./index
def index(request):
	return HttpResponse('Step 3. index view!')
	
# ./test
def test(request):
	return HttpResponse('Step 3. test view!')
```
In order to map urls to our view methods, we’ll need to configure them. Within our root URLs file within the demonstration folder, we’ll configure our urls to be proceeded by app/:
```python
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('app/', include('app.urls')),
]
```
Now, our URLs may be accessed as http://127.0.0.1:8000/app/<view url>. We’ll now create a new urls.py file within app/ like that:
```python
# app/urls.py
from django.conf.urls import url
from app import views

urlpatterns = [
	url('^$', views.index, name='index'),
	url('test/', views.test, name='test')
]
```
If we navigate to http://127.0.0.1:8000/app/test/, we should see the text “Step 3. test view!”.
Alright, we’ve been making some toy views, but how about we move onto displaying some meaningful data to the user? In particular, we’ll display the Github profile information for a given user.

## Step 4: Integrating the Github API
The Github API contains a collection of URLs which a developer can query using HTTP methods to retrieve data, in the form of JSON. In order to leverage this API, we’ll use the Python Requests library which will make this process simple. From the API for users, we can get profile information by using the following URL:
```
https://api.github.com/users/:user
```
Let’s go ahead and wire this up in Django. As an exercise, try to create the urls and view method before moving forward. Finally, navigating to http://127.0.0.1:8000/app/profile, at the moment the output is all the values with JSON types that we are interested in displaying to the user.

**Bower**
Bower is a front-end dependency manager for your project. In laymans terms, it is a command-line program which you can utilize to download libraries such as Twitter Bootstrap. The beauty of this approach is that we can generate a bower.json file, which any user can copy and use to download a bunch of packages easily - as opposed to going to each site, and manually copy/pasting/saving out files.

In this step, I’ll walk you through downloading Twitter bootstrap as well as generating your own bower.json. Before we do this, we’ll create a .bowerrc file.

In the same directory as manage.py, create a .bowerrc file with the following content:
```json
{
    "directory": "app/static/"
}
```
Anytime we run bower, it will output the downloaded files within the directory listed here. And now in our command line, we can simply run:
```bash
$ npm install -g bower
$ bower init
$ bower install bootstrap
$ bower install jquery
```
This will download Twitter Bootstrap into our project directory, as specified within our .bowerrc file.

## Step 5: Templating
Templates in Django are essentially HTML files which we pass in a context which then renders our data to the user. Before we can create our first template, we’ll need to create some folders. In the same directory as your  app/views.py:
```sh
$ mkdir templates
$ mkdir templates/app
$ cd templates/app
```
Within our templates/app folder, we’ll create our profile.html. Most of this is just Bootstrap classes for styling, but there is one important syntax to observe here:
```html
{% for key in data %}
{% endfor %
```
This syntax allows us to iterate over a data structure using a for loop, which should look familiar. Within this for loop, we do the following:
```html
    {{ key.name }}
    {{ key.blog }}
    {{ key.public_repos }}
    ...
```
In this case, data is an array of dictionaries, in which each dictionary has the name, blog, and public_repos keys (and a few others, listed in the above snippet for brevity). Here we access these properties and display them using the double curly braces syntax, which are template varaible placeholders which will take on the value of the expression within.

Apply method render for profile view:
```python
def profile(request):
    ...
    return render(request, './app/profile.html', {'data': parsedData})
```

With this new template in hand, let’s reload our profile page. Awesome, we’ve got a nice layout. As of now, our view method is essentially hardcoded - we can’t query any particular user’s Github information. We’ll need to come up with a way to ask the user for an input, and to do this we’ll move onto forms.

## Step 6: Forms
Forms are the bread and butter of web applications - every web programmer will come across them at one point or another. Forms essentially allow users to interact with your web application through various fields for input, usually for registration pages or in our case, performing a query.
To begin, we’ll go ahead and build our form within our profile.html:
```html
<style>
    .form-signin {
        max-width: 550px;
        padding: 15px;
        margin: 0 auto;
    }
</style>

<div class="container text-center">
	<form class="form-signin" id="login_form" method="post">
		<!-- protect against any cross site forgery attacks -->
		{% csrf_token %}
		
		<br>
		<!-- required autofocus: make a blue border around the form field when user has clicked to type -->
		<input type="text" name="user" class="form-control" placeholder="Github User Name, e.g: Oreder" value="" required autofocus />
		<br>
		<button class="btn" btn-lg btn-primary btn-block" type="submit">Get Data</button>
	</form>
</div>
```
Look at the input field, the most important attribute to pay attention to is name=user. This name parameter will have it’s value user sent as a POST parameter once the user submits the form, which we’ll get into shortly.

The last bit for our form is the actual submission, which will be a button, where here we provide attributes specifying the bootstrap styling class btn btn-lg btn-primary btn-block, as well as the type of action to perform when this button is clicked (in this case, a submit action.) Once this button is clicked, the form will be submitted and the values from it’s form fields (here we only have one form field) will be sent as a POST request to the corresponding URL set earlier.

## Step 7: Capturing POST parameters
As mentioned, performing a POST request will send parameters that can be accessed programmatically. Let’s modify our profilemethod within app/views.py to access the user value that was passed through our form submission:
```python
def profile(request):
	parsedData = []
	if request.method == 'POST':
		user = request.POST.get('user')
		jsonList = []
		req = requests.get('https://api.github.com/users/' + user)
		jsonList.append(json.loads(req.content))
		
		userData = {}
		for data in jsonList:
			userData['name'] = data['name']
			userData['blog'] = data['blog']
			userData['public_gists'] = data['public_gists']
			userData['public_repos'] = data['public_repos']
			userData['avatar_url'] = data['avatar_url']
			userData['followers'] = data['followers']
			userData['following'] = data['following']
			userData['location'] = data['location']
		
			parsedData.append(userData)
			
	return render(request, './app/profile.html', {'data': parsedData})
```
Likewise, we could write additional logic to handle cases for GET, UPDATE, and DELETE requests here based on the type of request we specified in our form.