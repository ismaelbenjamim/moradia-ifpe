from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView


class CustomisAuthenticated(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/error/403/")
        else:
            return super(CustomisAuthenticated, self).dispatch(request, *args, **kwargs)


class PaginaPrincipalView(LoginView):
    template_name = "pagina_principal.html"
    redirect_field_name = "admin"


class DashboardView(CustomisAuthenticated, TemplateView):
    template_name = "dashboard.html"


class NotPermissionView(TemplateView):
    template_name = "not_permission.html"


class CustomLogoutView(LogoutView):
    template_name = "logout.html"
