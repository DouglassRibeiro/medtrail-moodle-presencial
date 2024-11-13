from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage),
    path('homepage_register/', views.homepage_register, name='homepage_register'),
]
