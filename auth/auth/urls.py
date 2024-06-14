
from django.urls import path, include

urlpatterns = [
    path('', include('auth0.urls')),
]
