from . import views
from django.urls import path

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('usuario/cadastrar', views.cadastrar_usuario, name='usuario'),
    path ('livro/cadastrar', views.livro, name='livro'),
    path ('emprestimo' , views.emprestar, name='emprestimo'),
    path ('devolucao', views.devolucao, name='devolucao'),
    path ('reserva' , views.reservar, name='reserva'),
    path ('relatorio' , views.relatorio, name='relatorio'),
    
]