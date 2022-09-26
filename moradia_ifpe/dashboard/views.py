from django.views.generic import TemplateView

from moradia_ifpe.core.views import CustomIsAuthenticated


class DashboardView(CustomIsAuthenticated, TemplateView):
    template_name = "dashboard.html"


class GuideView(CustomIsAuthenticated, TemplateView):
    template_name = "dashboard.html"
