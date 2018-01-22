from django.forms import ModelForm

from django.shortcuts import render, redirect

from .models import *

from .forms import *

from django.contrib.auth.hashers import make_password

# Create your views here.

def index(request):
    contexto = {
    }
    return  render(request,"index.html", contexto)

def teste(request):
    return render(request, "teste.html", {})

def evento(request):
    contexto = {
        "eventos" : Evento.objects.all()
    }
    return render(request,"evento.html", contexto)

def registrar(request, template_name="registrar.html"):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.senha = make_password(request.POST['senha'])
        usuario.save()
        return redirect('usuario_registrado')
    return render(request, template_name, {'form':form})

 

def registrado(request, template_name="registrado.html"):

    return render(request, template_name)