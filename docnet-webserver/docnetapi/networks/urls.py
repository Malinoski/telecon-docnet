from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# Note:
# path(THE_URL_ACCESSED, THE_VIEW_USED, NICKNAME_TO_BE_USED_IN_OTHER_SERVER_POINTS),

'''
# URLs paths for function based views
urlpatterns = [
    path('networks/', views.network_list),
    path('networks/<int:pk>/', views.network_detail),
]
'''

'''
# URLs paths for class based views
urlpatterns = [
    path('', views.api_root),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('networks/', views.NetworkList.as_view(), name='network-list'),
    path('networks/<int:pk>/', views.NetworkDetail.as_view(), name='network-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('addresses/', views.AddressList.as_view(), name='address-list'),
    path('addresses/<int:pk>/', views.AddressDetail.as_view(), name='address-detail'),
]
'''

router = routers.DefaultRouter()
router.register('networks', views.NetworkView)
router.register('users', views.UserView)
router.register('addresses', views.AddressView)

# URLs paths for class based views
urlpatterns = [
   path('', include(router.urls))
]


# The code below allows to set a format in the url (like: http://127.0.0.1:8000/networks.json)
# urlpatterns = format_suffix_patterns(urlpatterns)
