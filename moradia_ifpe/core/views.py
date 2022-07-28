from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from moradia_ifpe.spreadsheet.forms import ImportSpreadForm
from moradia_ifpe.spreadsheet.models import SpreadSheet


class CustomIsAuthenticated(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/error/403/")
        else:
            return super(CustomIsAuthenticated, self).dispatch(request, *args, **kwargs)


class CustomLoginView(LoginView):
    template_name = "main_page.html"
    redirect_field_name = "admin"


class DashboardView(CustomIsAuthenticated, TemplateView):
    template_name = "dashboard.html"


class ImportSpreadSheetView(CreateView):
    model = SpreadSheet
    template_name = "import_spreadsheet.html"
    form_class = ImportSpreadForm
    success_url = ""

class NotPermissionView(TemplateView):
    template_name = "not_permission.html"


class CustomLogoutView(LogoutView):
    template_name = "logout.html"
