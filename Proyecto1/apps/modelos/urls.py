from django.urls import path
from apps.modelos.views import index

urlpatterns = {
    path("", index)
}