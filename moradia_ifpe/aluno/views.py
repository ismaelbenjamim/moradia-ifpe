import datetime

from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from moradia_ifpe.aluno.models import Aluno, Edital


class AlunoListView(ListView):
    model = Aluno
    queryset = Aluno.objects.all()
    template_name = "student/list.html"
    paginate_by = 10

    def get_queryset(self):
        if self.kwargs['edital'] == "ultimo":
            edital = Edital.objects.order_by('ano', 'periodo').latest('data_abertura')
            queryset = Aluno.objects.filter(edital=edital)
        else:
            edital_str = self.kwargs['edital']
            data_abertura = datetime.datetime.strptime(edital_str[7:], "%d%m%Y")
            edital = Edital.objects.filter(ano=edital_str[:4], periodo=edital_str[5:6], data_abertura=data_abertura)
            queryset = Aluno.objects.filter(edital__in=edital)
        self.queryset = queryset.order_by('pk')
        return super(AlunoListView, self).get_queryset()
