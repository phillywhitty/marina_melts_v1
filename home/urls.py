from django.urls import path
from . import views


# Defines URL patterns for managing shopping home app
urlpatterns = [
    path('', views.index, name='home')
]