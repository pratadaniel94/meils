from django.shortcuts import render

# Create your views here.

def index(request):
    contexto = {
    }
    return  render(request,"index.html", contexto)

def cadastro(request):
    contexto = {

    }
    return render (request,"cadastro.html", contexto)

def teste(request):
    return render(request, "teste.html", {})