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

# Remember, if classess was created or modified, syncronize it:
python manage.py makemigrations
python manage.py migrate

# Create the admin
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
```

* Run

```
python manage.py runserver 8001
```

* Tests from command line

Example 1: 

```
http -a admin:admin POST http://127.0.0.1:8001/networks/ title="New network" description="New description"
``` 
   
Example 2:

```
# Get token and save in $TOKEN
http post http://localhost:8001/api-token-auth/ username=admin password=admin

# Create a network (POST)
curl -d "title=New Network From Commanline&description2=New description from command line" -H "Authorization: Token $TOKEN" -X POST http://127.0.0.1:8001/networks/

# Edit a network (PUT)
curl -d "title=Updated the New Network From Commanline" -H "Authorization: Token $TOKEN" -X PUT http://127.0.0.1:8001/networks/1/

# Add an address for the network (POST)
curl -d "ip=10.0.0.0/31&description=Description of 10&title=Title of 10&network=http://localhost:8001/networks/1/" -H "Authorization: Token $TOKEN" -X POST http://127.0.0.1:8001/addresses/
  
```

* Test from Django REST Unit Tests
```
python manage.py test
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

* Destroy containers and image

```
docker stop docnet-webserver; docker rm docnet-webserver; docker rmi docnet-webserver_web
```

* Delete database and reconfigure.

```

rm -f db.sqlite3
rm -r networks/migrations
python manage.py makemigrations networks
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
echo "from django.contrib.auth.models import User; User.objects.create_superuser('user01', 'user01@example.com', 'user01')" | python manage.py shell

```
