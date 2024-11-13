from django.urls import path

from med.views import teste,homepage

urlpatterns = [
    path('homepage/', homepage),
    path('teste/', teste),
]
