from django.urls import path
from base import views

urlpatterns = [path("", views.lista_pendientes, name="pendientes")]