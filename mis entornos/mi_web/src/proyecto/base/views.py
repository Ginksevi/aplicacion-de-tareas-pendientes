from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Tarea

class lista_pendientes(ListView):
    model = Tarea
    context_object_name = "tareas"