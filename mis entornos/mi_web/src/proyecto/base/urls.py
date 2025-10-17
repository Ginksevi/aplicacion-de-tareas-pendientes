from django.urls import path
from .views import lista_pendientes, DetalleTarea

urlpatterns = [path("", lista_pendientes.as_view(), name="pendientes"),
               path("tarea/<int:pk", DetalleTarea.as_view(), name="tarea")]