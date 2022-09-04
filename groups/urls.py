from django.urls import path
from groups.views import create_Group, list_groups, delete_group, update_group
urlpatterns = [
    path("nuevo-grupo/", create_Group, name="create_group"),
    path("grupos-completo/", list_groups, name= "list-groups" ),
    path("borrar-grupo/<int:pk>/", delete_group, name="delete_group"),
    path("editar-grupo/<int:pk>/", update_group, name="update_group")
]
