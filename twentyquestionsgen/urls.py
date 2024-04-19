from django.urls import path, include
from .views import run

urlpatterns = [
    path('', run, name='run'),
]
