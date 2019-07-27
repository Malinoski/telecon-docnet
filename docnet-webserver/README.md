# Python web service

## Developement

* Install Python 3 and PyCharm CE 

* Create the PyCharm web sever project, using a new environment with Python 3 interpreter (i.e.: /usr/local/Cellar/python/3.7.4/bin/python3)

* Open the PyCharm Terminal and install the dependences:

```
pip install django
pip install djangorestframework
pip install django-cors-headers

```

* Create the project, app, etc..
```

# Create project and apps..
django-admin startproject [PROJECT_NAME] .
cd [PROJECT_NAME]
django-admin.py startapp [MY_APP]

# Create some code (settings, models, views, urls, etc..)
# ....

# Do not forget to sync models with database for the first time, ex.: 
python manage.py migrate
```

* Run

```
python manage.py runserver 8001
```

* Test from Command line

```
# Get token
http post http://localhost:8001/api-token-auth/ username=admin password=admin
# Use the token
http http://localhost:8001/hello/ 'Authorization: Token $TOKEN'
```

* Test from Django REST Unit Tests
```
# Test all
python manage.py test
```

## Deploy

* From Docker Compose:

```
# Run
docker-compose up -d
# Test (must return a token)
http post http://localhost:8001/api-token-auth/ username=admin password=admin
```

* To destroy the created containers and image docker

```
docker stop docnet-webserver; docker rm docnet-webserver; docker rmi docnet-webserver_web
```

