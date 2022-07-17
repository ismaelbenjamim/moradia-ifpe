from django.urls import path

from moradia_ifpe.core.views import PaginaPrincipalView, DashboardView, CustomLogoutView

urlpatterns = [
    path("", PaginaPrincipalView.as_view(), name='login'),
    path("dashboard/", DashboardView.as_view(), name='dashboard'),
    path("logout/", CustomLogoutView.as_view(), name='logout'),
]
