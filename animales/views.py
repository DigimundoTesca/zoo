from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal


def index(request):
    template = 'hola.html'
    return render(request, template, context=None)


def animales_vista(request):
    template = 'animales.html'
    animales = Animal.objects.all()
    context = {
        'animales': animales,
    }
    return render(request, template, context)
