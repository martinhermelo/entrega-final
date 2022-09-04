from django.urls import path
from estadios.views import create_stadium, list_stadiums, delete_stadium, update_stadium


urlpatterns= [
    path("crear-estadio/", create_stadium, name= "nuevo-estadio"),
    path("lista-estadios/", list_stadiums, name="lista-estadios"),
    path("borrar-estadio/<int:pk>/", delete_stadium, name="delete_stadium"),
    path("editar-estadio/<int:pk>/", update_stadium, name="update_stadium")
]

    # path("crear-estadio/", Create_stadium.as_view(), name="create_stadium"),
    # path("lista-estadios/", List_stadiums.as_view(), name="list_stadiums"),
    # path("borrar-estadio/<int:pk>", Delete_stadium.as_view(), name="delete_stadium