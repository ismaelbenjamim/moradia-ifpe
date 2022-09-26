from django.urls import path, include

from moradia_ifpe.aluno.views import AlunoListView


urlpatterns = [
    path(r"lista/<str:edital>/", AlunoListView.as_view(), name='aluno_list'),
]
