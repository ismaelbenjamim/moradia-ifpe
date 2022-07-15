from django.urls import path

from moradia_ifpe.core.views import PaginaPrincipalView

urlpatterns = [
    path("", PaginaPrincipalView.as_view()),
]
