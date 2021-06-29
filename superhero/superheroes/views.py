from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
from .models import Superhero
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404



def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, superhero_id):
    superhero_detail = Superhero.objects.get(pk=superhero_id)
    context = {
        'superhero_detail': superhero_detail
    }
    return render(request, 'superheroes/detail.html', context)

def edit(request, superhero_id):
    superhero_edit = Superhero.objects.get(pk=superhero_id)
    context = {
            'superhero_edit': superhero_edit
    }
    if request.method == 'POST':
        superhero_edit.name = request.POST.get('name')
        superhero_edit.alter_ego = request.POST.get('alter_ego')
        superhero_edit.primary_superhero_ability = request.POST.get('primary_superhero_ability')
        superhero_edit.secondary_superhero_ability = request.POST.get('secondary_superhero_ability')
        superhero_edit.catchphrase = request.POST.get('catchphrase')
        superhero_edit.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, "superheroes/edit.html", context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_superhero_ability = request.POST.get('primary_superhero_ability')
        secondary_superhero_ability = request.POST.get('secondary_superhero_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name,
                                  alter_ego=alter_ego,
                                  primary_superhero_ability=primary_superhero_ability,
                                  secondary_superhero_ability=secondary_superhero_ability,
                                  catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, "superheroes/create.html")

def delete(request, superhero_id):
    superhero_delete = Superhero.objects.get(pk=superhero_id)
    Superhero.objects.filter(pk=superhero_id).delete()
    context = {
        'superhero_delete': superhero_delete
    }
    return render(request, 'superheroes/delete.html', context)


