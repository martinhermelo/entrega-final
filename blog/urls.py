from django.urls import path
from blog.views import Create_note, List_notes, Delete_note, Detail_note
urlpatterns = [
    path("crear-nota/", Create_note.as_view(), name="create_note"),
    path("lista-notas/", List_notes.as_view(), name="list_note"),
    path("borrar-nota/<int:pk>/", Delete_note.as_view(), name="delete_note"),
    path("detalle-nota/<int:pk>/", Detail_note.as_view(), name="detail_note"),

]
