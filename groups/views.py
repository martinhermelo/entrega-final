from django.shortcuts import render, redirect
from groups.models import Groups
from groups.forms import Formulario_grupos
from django.contrib.auth.decorators import login_required

@login_required
def create_Group(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_grupos(request.POST)
            if form.is_valid():
                Groups.objects.create(
                    type = form.cleaned_data['type'],
                    team1 = form.cleaned_data['team1'],
                    team2 = form.cleaned_data['team2'],
                    team3 = form.cleaned_data['team3'],
                    team4= form.cleaned_data["team4"]
                )
                    
                return redirect(list_groups)

        elif request.method == 'GET':
            form = Formulario_grupos()
            context = {'form':form}
            return render(request, 'groups/new_group.html', context=context)
    return redirect("login")

@login_required
def list_groups(request):
    groups= Groups.objects.all()
    context= {
        "groups": groups
    }
    return render(request, "groups/all_groups.html",context=context)

@login_required
def delete_group(request, pk):
    if request.user.is_superuser:
        if request.method=="GET":
            group=Groups.objects.get(pk=pk)
            context={"group":group}
            return render(request, "groups/delete_group.html", context=context)
        elif request.method=="POST":
            group=Groups.objects.get(pk=pk)
            group.delete()
            return redirect(list_groups)
    return redirect("login")

@login_required
def update_group(request, pk):
    if request.user.is_superuser:
        if request.method=="POST":
            form= Formulario_grupos(request.POST)
            if form.is_valid():
                group= Groups.objects.get(pk=pk)
                group.type = form.cleaned_data['type']
                group.team1 = form.cleaned_data['team1']
                group.team2 = form.cleaned_data['team2']
                group.team3 = form.cleaned_data['team3']
                group.team4= form.cleaned_data["team4"]
                group.save()
                return redirect(list_groups)

        elif request.method =="GET":
            group= Groups.objects.get(pk=pk)
            form= Formulario_grupos(initial={
                                            "type": group.type,
                                            "team1": group.team1,
                                            "team2": group.team2,
                                            "team3": group.team3,
                                            "team4": group.team4,
                                            })
            context={"form":form}
            return render(request, "groups/update_group.html", context=context)
    return redirect("login")


