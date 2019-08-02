from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', include('networks.urls')),
]

urlpatterns += [

    # !WARNING!: No do use both api-auth and api-token-auth, but just one!
    # The api-auth not work well in browser (bug?)

    # Adding login to the Browsable API (remove rest_framework.authentication.TokenAuthentication' from settings!)
    # path('api-auth/', include('rest_framework.urls')),

    # Token REST login
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
