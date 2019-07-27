FROM python:3.6

# Environment Variables
ENV PYTHONUNBUFFERED 1

# Place to keep the project code
RUN mkdir /webapps

# Tell docker where to run the next commands
WORKDIR /webapps

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y libsqlite3-dev
RUN pip install -U pip setuptools

# Install python requirements
RUN pip install django
RUN pip install djangorestframework
RUN pip install django-cors-headers

# Include code in container
ADD . /webapps/

# Create some users (https://stackoverflow.com/questions/6244382/how-to-automate-createsuperuser-on-django)
WORKDIR /webapps/
# RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
# RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('user01', 'user01@example.com', 'user01')" | python manage.py shell

RUN python manage.py migrate
RUN python manage.py test docnetapi/networks

# Django service
EXPOSE 8001
