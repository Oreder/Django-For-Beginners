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