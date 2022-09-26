from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class CustomIsAuthenticated(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/error/403/")
        else:
            return super(CustomIsAuthenticated, self).dispatch(request, *args, **kwargs)


class CustomLoginView(LoginView):
    template_name = "login.html"
    redirect_field_name = "admin"


class CustomRegisterView(TemplateView):
    template_name = "register.html"
    redirect_field_name = "admin"


class NotPermissionView(TemplateView):
    template_name = "not_permission.html"


class CustomLogoutView(LogoutView):
    template_name = "logout.html"
