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



# Commands to deploy to AWS

After ssh into ubuntu image on aws run below command.

```python
 curl -sL  https://raw.githubusercontent.com/ravindra-gadiparthi/profile-rest-api/main/deploy/setup.sh  | sudo bash -
```

Note: update allowed hosts with ec2 hostname

```python
ALLOWED_HOSTS = ['ec2-13-127-54-108.ap-south-1.compute.amazonaws.com', 'localhost']
```

# Popular packages to look into 

Django Database Models [django.db.models](https://docs.djangoproject.com/en/3.1/topics/db/models/)

## Generating SSH Key pair and importing to Github Account

 
 [Generating SSH Key Pair](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
 
 [Importing key pair to Github Account](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)
 
 [Testing connection to github](https://docs.github.com/en/github/authenticating-to-github/testing-your-ssh-connection)
