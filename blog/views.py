from blog.models import Notes
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView


class Create_note(CreateView):
    model= Notes
    template_name="notes/create_note.html"
    fields= "__all__"
    success_url= "/notes/lista-notas/"

class List_notes(ListView):
    model=Notes
    template_name="notes/list_notes.html"

class Delete_note(DeleteView):
    model= Notes
    template_name="notes/delete_note.html"
    success_url= "/notes/lista-notas/"


class Detail_note(DetailView):
    model= Notes
    template_name="notes/detail_note.html"