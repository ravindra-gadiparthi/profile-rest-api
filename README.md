# profile-rest-api

## create virtual environment and install dependencies

```bash
pipenv install -r requirements.txt
```

## Launch virtual environment

```bash
pipenv shell
```

## create django project

with . you are asking django admin to create project in root repository.

```bash
django-admin startproject profile_project .
```

## create django app

```bash
python manage.py startapp profile_api
```

## creating models and sync with database

After creating models object use below commands to sync with database

create migrations

```bash
python manage.py makemigrations profile_api 
```

migrate models to database

```bash
python manage.py migrate
```

## creating is_superuser

```bash
python manage.py createsuperuser
```
super user created this project is
email: ravindra@gmail.com
password: Ravi@123
## registering models to admin console

``` python
from django.contrib import admin
## import required models
from profile_api import models

admin.site.register(models.UserProfile)
```
