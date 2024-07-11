from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_username, name='input_username'),
]