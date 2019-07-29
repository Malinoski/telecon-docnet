from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

'''
# URLs for function based views
urlpatterns = [
    path('networks/', views.network_list),
    path('networks/<int:pk>/', views.network_detail),
]
'''

# URLs for class based views
# path(THE_URL_ACCESSED, THE_VIEW_USED, NICKNAME_TO_BE_USED_IN_OTHER_SERVER_POINTS),
urlpatterns = [
    path('', views.api_root),
    path('networks/', views.NetworkList.as_view(), name='network-list'),
    path('networks/<int:pk>/', views.NetworkDetail.as_view(), name='network-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('hello/', views.HelloView.as_view(), name='hello'),
]

# The code below allows to set a format in the url (like: http://127.0.0.1:8000/networks.json)
urlpatterns = format_suffix_patterns(urlpatterns)
