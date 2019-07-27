from django.contrib import admin
from django.urls import path, include
from docnetapi.core import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('', admin.site.urls),
    path('', include('docnetapi.networks.urls')),
    path('hello/', views.HelloView.as_view(), name='hello'),
]
