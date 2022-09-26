from django.urls import path, include

from moradia_ifpe.dashboard.views import DashboardView, GuideView

urlpatterns = [
    path("", DashboardView.as_view(), name='dashboard'),
    path("guia/", GuideView.as_view(), name='guide'),
    path("alunos/", include("moradia_ifpe.aluno.urls")),
]
