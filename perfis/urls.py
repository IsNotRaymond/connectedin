from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('perfil/<int:id_perfil>', exibir, name='exibir-perfil'),
    path('perfil/<int:id_perfil>/convidar', convidar, name='convidar-perfil'),
    path('convite/<int:id_convite>/aceitar', aceitar, name='aceitar-convite')
]
