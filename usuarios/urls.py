from django.urls import path
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login.html'), name='logout'),
]
