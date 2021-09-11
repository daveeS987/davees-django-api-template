# Davee's Django Rest API Template

## Author: Davee Sok

## Links & Resources

- [Creating a Custom User](https://testdriven.io/blog/django-custom-user-model/)

## Overview/ Motivation

work in progess....

Starting up a Django api can be time consuming. This template is meant to get up and running fast

## Tools & Dependencies

- Django
- Django Rest Framework
- Black
- Docker

## Getting Started

- Create a New Secret key by running the following command in the terminal:

```iterm
python -c 'from django.core.management.utils import get_random_secret_key; \
            print(get_random_secret_key())'
```

- You will get a 50 digit key, replace settings.py line 23 with the new key

```python
SECRET_KEY = "django-insecure-INSERT_NEW_SECRET_KEY_HERE"
```

- The name of the example model is called "Example". Do a global search of "Example" and replace all occurences with a model name that you want. Remember to "Match Case" and "Match Whole Word"

- In terminal run the following commands:

```iterm
poetry install
python manage.py makemigrations
python manage.py migrate
```

### Other Commands To Know

```python
poetry export -f requirements.txt -o requirements.txt
docker-compose up
docker-compose -d
docker-compose down
docker-compose logs
docker-compose up --build
```
