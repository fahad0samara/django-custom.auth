# custom_app/urls.py
from django.urls import path
from .views import register, user_login, user_logout, home, user_profile

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('user_profile/', user_profile, name='user_profile'),

]

