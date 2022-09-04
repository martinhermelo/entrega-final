from django.shortcuts import render, redirect
from estadios.models import Estadios
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DeleteView

from estadios.forms import Formulario_estadios

@login_required
def create_stadium(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_estadios(request.POST, request.FILES)
            if form.is_valid():
                Estadios.objects.create(
                    name = form.cleaned_data['name'],
                    image = form.cleaned_data['image'],
                )
                    
                return redirect(list_stadiums)

        elif request.method == 'GET':
            form = Formulario_estadios()
            context = {'form':form}
            return render(request, 'estadios/create_stadium.html', context=context)
    return redirect("login")

@login_required
def list_stadiums(request):
    stadiums= Estadios.objects.all()
    context= {
        "stadiums": stadiums
    }
    return render(request, "estadios/list_stadiums.html",context=context)

@login_required
def delete_stadium(request, pk):
    if request.user.is_superuser:
        if request.method=="GET":
            stadium=Estadios.objects.get(pk=pk)
            context={"stadium":stadium}
            return render(request, "estadios/delete_stadium.html", context=context)
        elif request.method=="POST":
            stadium=Estadios.objects.get(pk=pk)
            stadium.delete()
            return redirect(list_stadiums)
    return redirect("login")

@login_required
def update_stadium(request, pk):
    if request.user.is_superuser:
        if request.method=="POST":
            form= Formulario_estadios(request.POST, request.FILES)
            if form.is_valid():
                stadium= Estadios.objects.get(pk=pk)
                stadium.name = form.cleaned_data['name']
                stadium.image= form.cleaned_data["image"]
                stadium.save()
                return redirect(list_stadiums)

        elif request.method =="GET":
            stadium= Estadios.objects.get(pk=pk)
            form= Formulario_estadios(initial={
                                            "name":stadium.name,
                                            "image":stadium.image
                                            })
            context={"form":form}
            return render(request, "estadios/update_stadium.html", context=context)
    return redirect("login")






