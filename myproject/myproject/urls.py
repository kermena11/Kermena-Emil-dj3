from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myuser.urls')),
    path('track/', include('tracks.urls')),
    path('trainee/', include('trainee.urls')),
]
