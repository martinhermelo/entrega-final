from django.shortcuts import render, redirect
from plantel.models import Plantel
from plantel.forms import Formulario_jugadores


from django.contrib.auth.decorators import login_required


def template_prueba(request):
    if request.user.is_superuser:
        context= {
            "name": "Martin",
            "last_name" : "Hermelo",
            "qatar": "Qatar"
        }
        return render(request, "primertemplate.html", context=context)
    return redirect("login")

@login_required
def create_player(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_jugadores(request.POST, request.FILES)
            if form.is_valid():
                Plantel.objects.create(
                    full_name = form.cleaned_data['full_name'],
                    height = form.cleaned_data['height'],
                    age = form.cleaned_data['age'],
                    club = form.cleaned_data['club'],
                    skillfull_leg= form.cleaned_data["skillfull_leg"],
                    position= form.cleaned_data['position'],
                    image= form.cleaned_data["image"]
                )
                    
                return redirect(list_players)
        elif request.method == 'GET':
            form = Formulario_jugadores()
            context = {'form':form}
            return render(request, 'plantel/new_player.html', context=context)
    return redirect("login")

@login_required
def list_players(request):
    players= Plantel.objects.all()
    context= {
        "players": players
    }
    return render(request, "plantel/players_list.html",context=context)

@login_required
def primer_formulario(request):
    if request.user.is_superuser:
        print(request.method)
        if request.method == 'POST':
            print(request.POST)
        return render(request, 'plantel/primer_formulario.html', context={})
    return redirect("login")

@login_required
def delete_player(request, pk):
    if request.user.is_superuser:
        if request.method=="GET":
            player=Plantel.objects.get(pk=pk)
            context={"player":player}
            return render(request, "plantel/delete_player.html", context=context)
        elif request.method=="POST":
            player=Plantel.objects.get(pk=pk)
            player.delete()
            return redirect(list_players)
    return redirect("login")

@login_required
def update_player(request, pk):
    if request.user.is_superuser:
        if request.method=="POST":
            form= Formulario_jugadores(request.POST, request.FILES)
            if form.is_valid():
                player= Plantel.objects.get(pk=pk)
                player.full_name = form.cleaned_data['full_name']
                player.height = form.cleaned_data['height']
                player.age = form.cleaned_data['age']
                player.club = form.cleaned_data['club']
                player.skillfull_leg= form.cleaned_data["skillfull_leg"]
                player.position= form.cleaned_data['position']
                player.image= form.cleaned_data["image"]
                player.save()
                return redirect(list_players)

        elif request.method =="GET":
            player= Plantel.objects.get(pk=pk)
            form= Formulario_jugadores(initial={
                                            "full_name": player.full_name,
                                            "height": player.height,
                                            "age": player.age,
                                            "club": player.club,
                                            "skillfull_leg": player.skillfull_leg,
                                            "position": player.position,
                                            "image": player.image
                                            })
            context={"form":form}
            return render(request, "plantel/update_player.html", context=context)
    return redirect("login")




