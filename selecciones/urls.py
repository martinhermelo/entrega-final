from django.urls import path
from selecciones.views import create_team, list_teams, delete_team, update_team

urlpatterns = [
    path("equipo-nuevo/", create_team, name="newteam"),
    path("lista-equipos/",list_teams, name="allteams"),
    path("borrar-equipo/<int:pk>/", delete_team, name="delete_team"),
    path("editar-equipo/<int:pk>/", update_team, name="update_team")
] 
