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
urlpatterns = [
    path('networks/', views.NetworkList.as_view()),
    path('networks/<int:pk>/', views.NetworkDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

# The code below allows to set a format in the url (like: http://127.0.0.1:8000/networks.json)
urlpatterns = format_suffix_patterns(urlpatterns)
