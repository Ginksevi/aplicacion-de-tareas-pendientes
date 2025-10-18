from django.urls import path
from .views import lista_pendientes, DetalleTarea, CrearTarea

urlpatterns = [path("", lista_pendientes.as_view(), name="pendientes"),
               path("tarea/<int:pk", DetalleTarea.as_view(), name="tarea"),
               path("crear_tarea/", CrearTarea.as_view(), name="crear_tarea")]
