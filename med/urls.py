from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage_register/', views.homepage_register, name='homepage_register'),
    path('just_register/', views.just_register, name='just_register'),
]
