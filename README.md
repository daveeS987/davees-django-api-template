# Davee's Django Rest API Template

## Author: Davee Sok

## Links & Resources

- [Django](https://docs.djangoproject.com/en/3.2/)
- [Django Rest Framework](https://www.django-rest-framework.org/)

## Overview/ Motivation

work in progess....

Starting up a Django api can be time consuming. This template is meant to get up and running fast

## Tools & Dependencies

- Django
- Django Rest Framework
- Black
- Docker

## Getting Started

### Create a New Secret Key by running the following command in the terminal:

```iterm
python -c 'from django.core.management.utils import get_random_secret_key; \
            print(get_random_secret_key())'
```

### You will get a 50 digit key. Add new key to settings.py line 23

```python
SECRET_KEY = "django-insecure-INSERT_NEW_SECRET_KEY_HERE"
```

### The name of the example model is called "Example". Replace all occurences

- Do a global search of "Example" and replace all occurences with a model name that you want. Remember to "Match Case" and "Match Whole Word". You need to use a capital letter for this step

- now replace Example folder name (this can be lowercase)

  - needs to match name on line 6 in app.py
  - needs to match urlpatterns on line 19 in a_project.settings.py

### In terminal run the following commands:

```iterm
poetry install
python manage.py makemigrations
python manage.py migrate
```

#### Other Commands To Know

```python
poetry export -f requirements.txt -o requirements.txt
docker-compose up
docker-compose -d
docker-compose down
docker-compose logs
docker-compose up --build
```
