from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView


class PaginaPrincipalView(LoginView):
    template_name = "pagina_principal.html"
    redirect_field_name = "admin"

