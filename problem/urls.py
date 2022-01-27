from django.urls import path
from . import views

urlpatterns = [
    path('', views.problemList, name='problemList'),
]