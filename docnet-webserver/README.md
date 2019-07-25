# Python web service

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
python manage.py startapp [MY_APP]

# Create some code (settings, models, views, urls, etc..)
# ....

# Do not forget to sync models with database for the first time, ex.: 
python manage.py migrate
```

* Run

```
python manage.py runserver 8001
```

* Test

http://127.0.0.1:9001/hello/