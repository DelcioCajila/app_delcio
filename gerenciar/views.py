
from django.shortcuts import render
from django.shortcuts import render

def pagina_inicial(request): 
   return render (request, 'home.html')

def cadastrar_usuario(request): 
   return render (request, 'usuario.html')
 
def livro(request): 
   return render (request, 'livro.html')

 
def emprestar(request): 
   return render (request, 'emprestimo.html')


def devolucao (request): 
   return render (request, 'devolucao.html')

def reservar (request): 
   return render (request, 'reserva.html')


def relatorio (request): 
   return render (request, 'relatorio.html')


