from django.shortcuts import render, redirect
from groups.views import Groups
from selecciones.views import Selecciones
from plantel.views import Plantel
from estadios.views import Estadios
from blog.views import Notes
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,"index.html")

@login_required
def search_all(request):
        search= request.GET["search"]
        players = Plantel.objects.filter(full_name__icontains=search)
        groups = Groups.objects.filter(type__icontains=search)
        teams= Selecciones.objects.filter(name__icontains=search)
        stadiums= Estadios.objects.filter(name__icontains=search)
        notes= Notes.objects.filter(author__icontains=search)
        context= {
            "players": players,
            "groups": groups,
            "teams": teams,
            "stadiums":stadiums,
            }
        return render(request,"search.html", context=context)
