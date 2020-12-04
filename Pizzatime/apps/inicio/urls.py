from django.urls import path
from apps.inicio.views import inicio

urlpatterns = [
    path('', inicio)
]