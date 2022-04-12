from django.urls import path
from . import views

urlpatterns = [
    path('create', views.MatchCreate.as_view(), name='MatchCreate'),
]
