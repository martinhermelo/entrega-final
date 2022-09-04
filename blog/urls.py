from django.urls import path
from blog.views import Create_note, List_notes, Delete_note

urlpatterns = [
    path("crear-nota/", Create_note.as_view(), name="create_stadium"),
    path("lista-notas/", List_notes.as_view(), name="list_stadiums"),
    path("borrar-nota/<int:pk>/", Delete_note.as_view(), name="delete_stadium")
]
