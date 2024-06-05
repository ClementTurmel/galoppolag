# galoppolag
A project to experiment Django python framework


## requirement
* python
    * for me `python --version` -> Python 3.12.3
* Django
    * `python -m pip install Django` -> Successfully installed Django-5.0.6 asgiref-3.8.1 sqlparse-0.5.0 tzdata-2024.1
    * `python -m django --version` -> 5.0.6
* Postgres

## steps I followed 

installation : https://docs.djangoproject.com/en/5.0/topics/install/#installing-official-release
tutorial : https://docs.djangoproject.com/en/5.0/intro/tutorial01/

create django project : `django-admin startproject galoppolag`

move to project dir and start server : `python manage.py runserver` (ignoring unapplied migrations for now) and check `127.0.0.1:8000`

create a app : `python manage.py startapp equines`

create file `equines/urls.py` file and add coresponding code according to tutorial in `equines/urls.py` and `galoppolag/urls.py`, start server and check `http://127.0.0.1:8000/equines/`

