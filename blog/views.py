from django.shortcuts import render, redirect
from blog.models import Notes
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView
from django.contrib.auth.decorators import login_required

from blog.forms import Formulario_notas

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

@login_required
def update_note(request, pk):
    if request.user.is_superuser:
        if request.method=="POST":
            form= Formulario_notas(request.POST)
            if form.is_valid():
                note= Notes.objects.get(pk=pk)
                note.title = form.cleaned_data['title']
                note.description = form.cleaned_data['description']
                note.author = form.cleaned_data['author']
                note.email = form.cleaned_data['email']
                note.save()
                return redirect("/notes/lista-notas/")

        elif request.method =="GET":
            note= Notes.objects.get(pk=pk)
            form= Formulario_notas(initial={
                                            "title": note.title,
                                            "description": note.description,
                                            "author": note.author,
                                            "email": note.email,
                                            })
            context={"form":form}
            return render(request, "notes/update_note.html", context=context)
    return redirect("login")