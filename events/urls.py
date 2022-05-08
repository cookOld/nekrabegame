from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index),
    path("create/",views.create),
    path('<int:pk>/', views.info),
    path('<int:pk>/request/', views.e_request),
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/prof/', views.prof),
    path('<int:pk>/prof/add/', views.add),
]