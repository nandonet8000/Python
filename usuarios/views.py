from django.shortcuts import render
from django.http import HttpRequest
from usuarios.forms import CadastroForms, LoginForm

def login(request: HttpRequest):
    form = LoginForm()
    return render(request, "usuarios/login.html", {"form": form})


def cadastro(request : HttpRequest) :

        form = CadastroForms()
        
        return render(request, "usuarios/cadastro.html", {"form" : form})
