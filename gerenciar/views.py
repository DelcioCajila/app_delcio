
from django.shortcuts import render
from django.shortcuts import render

def pagina_inicial(request): 
   return render (request, 'home.html')

def cadastrar(request): 
   return render (request, 'cadastrar.html')
 
 
def eliminar(request): 
   return render (request, 'eliminar.html')

 
def editar(request): 
   return render (request, 'editar.html')

 
def atualizar(request): 
   return render (request, 'atualizar.html')