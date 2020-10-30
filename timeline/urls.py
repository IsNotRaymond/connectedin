from django.urls import path
from .views import CriarPostagem, postagens, detail_postagem

urlpatterns = [
    path('criar-postagem/', CriarPostagem.as_view(), name='criar-postagem'),
    path('postagem/<int:id_postagem>', detail_postagem, name='exibir-postagem'),
    path('timeline/', postagens, name='timeline')
]
