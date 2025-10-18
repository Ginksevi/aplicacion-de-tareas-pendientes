from django.urls import path
from .views import lista_pendientes, DetalleTarea, CrearTarea, EditarTarea,EliminarTarea, Logueo
from django.contrib.auth.views import LogoutView

urlpatterns = [path("", lista_pendientes.as_view(), name="tareas"),
               path("login/", Logueo.as.view(), name = "login"),
               path("logout/", LogoutView.as.view(next_page = "login"), name = "logout"),
               path("tarea/<int:pk", DetalleTarea.as_view(), name="tarea"),
               path("crear_tarea/", CrearTarea.as_view(), name="crear_tarea"),
               path("editar_tarea/<int:pk", EditarTarea.as_view(), name="editar_tarea"),
               path("eliminar_tarea/<int:pk", EliminarTarea.as_view(), name="eliminar_tarea")]
