from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Superhero
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# def index(request):
#     return render(request, 'superheroes/index.html')

def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, superhero_id):
    superhero_detail = Superhero.objects.get()
    context = {
        'superhero_detail': superhero_detail
    }
    return render(request, 'superheroes/detail.html', context)
    pass

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


