# galoppolag
A project to experiment Django python framework


## requirement
* python
    * for me `python --version` -> Python 3.12.3
* Django
    * `python -m pip install Django` -> Successfully installed Django-5.0.6 asgiref-3.8.1 sqlparse-0.5.0 tzdata-2024.1
    * `python -m django --version` -> 5.0.6
* for database, Sqlite fow now, already configured by default by Django

## steps I followed 

installation : https://docs.djangoproject.com/en/5.0/topics/install/#installing-official-release


[tutorial part 1 :](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)

create django project : `django-admin startproject galoppolag`

move to project dir and start server : `python manage.py runserver` (ignoring unapplied migrations for now) and check `127.0.0.1:8000`

create a app : `python manage.py startapp equines`

create file `equines/urls.py` file and add coresponding code according to tutorial in `equines/urls.py` and `galoppolag/urls.py`, start server and check `http://127.0.0.1:8000/equines/`

[part 2](https://docs.djangoproject.com/fr/5.0/intro/tutorial02/)

some INSTALLED_APPS from galoppolag/settings.py need database access with tables created so we run `python manage.py migrate`to create them.

I create `Equine` and `Person` class in `equines/models.py` and run `python manage.py makemigrations equines`. 
this command has produce a `0001_initial.py` file with information about our models (the creation of them in this case).

I run the command `python manage.py sqlmigrate equines 0001` and it show SQL instruction creating tables Person and Equine.

command `python manage.py check` check project conformity without applying migration or modifying database.

To create tables  `Equine` and `Person` in database, I run `python manage.py migrate` and it `return Applying equines.0001_initial... OK`. tables are now visible (using DBeaver for example)