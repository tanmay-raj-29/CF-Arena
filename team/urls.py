from django.urls import path
from . import views

urlpatterns = [
    path('create', views.TeamCreate.as_view(), name='TeamCreate'),
]
