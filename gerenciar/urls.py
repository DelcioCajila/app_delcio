from . import views
from django.urls import path

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('usuario/cadastrar', views.cadastrar, name='cadastrat'),
    path ('usuario/eliminar', views.eliminar, name='eliminar'),
    path ('usuario/editar', views.editar, name='usuario'),
    path ('usuario/atualizar', views.atualizar, name='atualizar')
]