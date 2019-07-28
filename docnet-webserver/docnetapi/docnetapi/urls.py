from django.urls import path, include

urlpatterns = [
    path('', include('networks.urls')),
]

# Adding login to the Browsable API
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
