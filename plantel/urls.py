from django.urls import path
from plantel.views import create_player, list_players, primer_formulario, delete_player, update_player


urlpatterns = [
    path("jugador/", create_player, name= "newplayer"),
    path("equipo/", list_players, name="plantel"),
    path("primer-formulario/", primer_formulario, name="primer_formulario"),
    path("borrar-jugador/<int:pk>/", delete_player, name="delete_player"),
    path("editar-jugador/<int:pk>/", update_player, name="update_player")
]
