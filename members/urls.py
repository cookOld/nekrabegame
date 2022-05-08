from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users/', views.users),
    path('<int:pk>/', views.member),
]