from django.contrib import admin
from django.urls import path, include
from docnetapi.core import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', admin.site.urls),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('network_app/', include('docnetapi.networks.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
