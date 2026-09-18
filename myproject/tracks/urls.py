from django.urls import path
from .views import alltracks, gettrack, createtrack, updatetrack, deletetrack

urlpatterns = [
    path("", alltracks, name="alltracks"),
    path("create/", createtrack, name="createtrack"),
    path("<int:id>/", gettrack, name="gettrack"),
    path("update/<int:id>/", updatetrack, name="updatetrack"),
    path("delete/<int:id>/", deletetrack, name="deletetrack"),
]
