# Python web service

## Developement

* Install Python 3 and PyCharm CE 

* Create the PyCharm web sever project, using a new environment with Python 3 interpreter (i.e.: /usr/local/Cellar/python/3.7.4/bin/python3)

* Open the PyCharm Terminal and install the dependences:

```
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install pygments

```

* Create the project, app, etc..
```

# Create project and apps..
django-admin startproject [PROJECT_NAME] .
django-admin.py startapp [MY_APP]

# Create some code (settings, models, views, urls, etc..)
# ....

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
python manage.py test docnetapi/networks
```

## Deploy

* From Docker Compose:

```
# Run
docker-compose up -d
# Note: To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
# Test (must return a token)
http post http://localhost:8001/api-token-auth/ username=admin password=admin
```

## Utils

* To destroy the containers and the image Docker

```
docker stop docnet-webserver; docker rm docnet-webserver; docker rmi docnet-webserver_web
```

* To delete the database and start again.
```
rm -f db.sqlite3
rm -r networks/migrations
python manage.py makemigrations networks
python manage.py migrate
```