from django.shortcuts import render, redirect
from blog.models import Notes
from django.views.generic import CreateView, ListView, DeleteView


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