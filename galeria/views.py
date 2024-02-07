from django.shortcuts import render
from django.http import HttpResponse
from calcularData import test_automatizado
# Create your views here.



def index(request):
    dados = {
    1 : {"nome" :  "Nebulosa de Carina",
         "legenda" : "webbtelecope.org /NASA/ James Webb",
         "relogio" : test_automatizado()
         },

    2 : {"nome" : "Galaxia NGC 1079",
         "legenda" : "nasa.org /NASA / Hubble",
         "relogio" : test_automatizado()}

    }
    return render(request, 'galeria/index.html', {"cards" : dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')
    

