from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('networks', views.NetworkView)
router.register('users', views.UserView)
router.register('addresses', views.AddressView)

# URLs paths for classes based views
urlpatterns = [
   path('', include(router.urls))
]
