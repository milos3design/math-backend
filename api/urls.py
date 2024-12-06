from django.urls import path, include
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]