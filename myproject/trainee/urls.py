from django.urls import path
from .views import home, profile
urlpatterns=[path('',home,name='trainee_home'),path('profile/',profile,name='trainee_profile')]
