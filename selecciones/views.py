from django.shortcuts import render, redirect
from selecciones.models import Selecciones
from selecciones.forms import Formulario_selecciones
from django.contrib.auth.decorators import login_required


@login_required
def create_team(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_selecciones(request.POST)
            if form.is_valid():
                Selecciones.objects.create(
                    name = form.cleaned_data['name'],
                    federation = form.cleaned_data['federation'],
                )
                return redirect(list_teams)
        elif request.method == 'GET':
            form = Formulario_selecciones()
            context = {'form':form}
            return render(request, 'selecciones/new_team.html', context=context)
    return redirect("login")

@login_required
def list_teams(request):
    teams= Selecciones.objects.all()
    context= {
        "teams": teams
    }
    return render(request, "selecciones/all_teams.html",context=context)

@login_required
def delete_team(request, pk):
    if request.user.is_superuser:
        if request.method=="GET":
            team=Selecciones.objects.get(pk=pk)
            context={"team":team}
            return render(request, "selecciones/delete_team.html", context=context)
        elif request.method=="POST":
            team=Selecciones.objects.get(pk=pk)
            team.delete()
            return redirect(list_teams)
    return redirect("login")

@login_required
def update_team(request, pk):
    if request.user.is_superuser:
        if request.method=="POST":
            form= Formulario_selecciones(request.POST)
            if form.is_valid():
                team= Selecciones.objects.get(pk=pk)
                team.name= form.cleaned_data["name"]
                team.federation= form.cleaned_data["federation"]
                team.save()
                return redirect(list_teams)

        elif request.method =="GET":
            team= Selecciones.objects.get(pk=pk)
            form= Formulario_selecciones(initial={
                                            "name": team.name,
                                            "federation": team.federation})
            context={"form":form}
            return render(request, "selecciones/update_selecciones.html", context=context)
    return redirect("login")
