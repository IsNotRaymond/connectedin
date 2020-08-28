from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('perfil/<int:id_perfil>', exibir),
]