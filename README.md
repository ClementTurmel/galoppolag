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

##### installation : 
https://docs.djangoproject.com/en/5.0/topics/install/#installing-official-release


##### [tutorial part 1 :](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)

create django project : `django-admin startproject galoppolag`

move to project dir and start server : `python manage.py runserver` (ignoring unapplied migrations for now) and check `127.0.0.1:8000`

create a app : `python manage.py startapp equines`

create file `equines/urls.py` file and add coresponding code according to tutorial in `equines/urls.py` and `galoppolag/urls.py`, start server and check `http://127.0.0.1:8000/equines/`

##### [part 2](https://docs.djangoproject.com/fr/5.0/intro/tutorial02/)

some INSTALLED_APPS from galoppolag/settings.py need database access with tables created so we run `python manage.py migrate`to create them.

I create `Equine` and `Person` class in `equines/models.py` and run `python manage.py makemigrations equines`. 
this command has produce a `0001_initial.py` file with information about our models (the creation of them in this case).

I run the command `python manage.py sqlmigrate equines 0001` and it show SQL instruction creating tables Person and Equine.

command `python manage.py check` check project conformity without applying migration or modifying database.

To create tables  `Equine` and `Person` in database, I run `python manage.py migrate` and it `return Applying equines.0001_initial... OK`. tables are now visible (using DBeaver for example)

creating data through shell :
execute command `python manage.py shell` and then :
```
>>> from equines.models import Equine, Person
>>> Person.objects.all()
<QuerySet []>
>>> p = Person(first_name="Clément", last_name="Turmel", email="a@b.c", phone="0123456789")
>>> p.save()
>>> p.id
1
>>> Person.objects.all()
<QuerySet [<Person: Person object (1)>]>
>>> p.first_name 
'Clément'
>>> p.email = "d@e.f"
>>> p.save()
```

I also try to use same operation using test, see [commit test_person.py](https://github.com/ClementTurmel/galoppolag/commit/ed5d7f653867bd13549da999c6f9530b6c523c95#diff-e951cc5abe15ddb4612556321cd5170908a0c2962a54c1ad86175b953657f1d5) (run test using command `python manage.py test`)
with default sqlite database, for test, a in-memory database is used, data are hermetic between test and memory database is destroyed after test execution.

Next I explore filter (see `test_equine.py`), I see that I can't save a `equine` object if the attribute `owner` of it (a `Person` object) is not saved before.

I also noticed that 'models.ForeignKey' type of attribute owner make the attribute mandatory for saving.
We saw it before, doing the command `python manage.py sqlmigrate equines 0001` that colunm "owner_id" was NOT NULL. (TODO explore if a 'models.ForeignKey' can be nullable)

##### [part 2: administration](https://docs.djangoproject.com/fr/5.0/intro/tutorial02/#creating-an-admin-user)

I create a admin user, and register Equine and Person classes from model in admin.py to be able to add/edit/remove them in the django admin page `http://127.0.0.1:8000/admin/ `

##### Modifying the model :

I add a field birthday in person class, that throw a `django.db.utils.OperationalError: no such column: equines_person.birthday` when refreshing the server
wich seems normal since a do not migrate the model for now.
so I try a migration : `python manage.py makemigrations equines`
that say : 
```
It is impossible to add a non-nullable field 'birthday' to person without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 1
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>>"2019-01-02" 
```
then I check sql script using `python manage.py sqlmigrate equines 0002`

then python manage.py check

and then python manage.py migrate

