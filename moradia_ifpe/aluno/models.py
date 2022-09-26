from django.core.validators import MinLengthValidator
from django.db import models
from uuid import uuid4

from moradia_ifpe.aluno.functions.getpoints import getPoints


class Edital(models.Model):
    ano = models.CharField("Ano", validators=[MinLengthValidator(4)], max_length=4)
    periodo = models.CharField("Período", validators=[MinLengthValidator(1)], max_length=2)
    data_abertura = models.DateField("Data de abertura")

    def __str__(self):
        return f"{str(self.ano)}.{str(self.periodo)}"

    class Meta:
        unique_together = ['ano', 'periodo', 'data_abertura']


class Aluno(models.Model):
    nome_completo = models.CharField(verbose_name='Nome completo', max_length=255)
    matricula = models.CharField(verbose_name='Matrícula', max_length=30, null=True, blank=True)
    cpf = models.CharField(verbose_name='CPF', unique=True, max_length=20)
    curso = models.CharField(verbose_name='Curso', max_length=255, null=True, blank=True)
    data_criacao = models.DateTimeField(verbose_name="Data de criação", null=True, blank=True)
    passo = models.CharField(verbose_name='Passo', max_length=255, null=True, blank=True)
    renda_per_capita = models.FloatField(verbose_name='Renda per capita', null=True, blank=True)
    cotista = models.BooleanField(verbose_name='É cotista', default=False)
    beneficiario_bolsa_social = models.CharField(verbose_name='Beneficiário', max_length=255, null=True, blank=True)
    raca = models.CharField(verbose_name='Raça', max_length=255, null=True, blank=True)
    ultimo_login = models.DateTimeField(verbose_name='Último login', null=True, blank=True)
    origem_escolar = models.CharField(verbose_name='Origem escolar', max_length=255, null=True, blank=True)
    orientacao_sexual = models.CharField(verbose_name='Orientação sexual', max_length=255, null=True, blank=True)
    regiao_moradia = models.CharField(verbose_name='Região de moradia', max_length=100, null=True, blank=True)
    quantidade_filhos = models.IntegerField(verbose_name='Quantidade de filhos entre 0 e 6 anos', null=True, blank=True)
    quantidade_pessoas_familia = models.IntegerField(verbose_name='Quantas pessoas compõem o núcleo familiar', null=True, blank=True)
    quantidade_materias_periodo = models.IntegerField(verbose_name='Quantidade de matérias no período', null=True, blank=True)
    comentario = models.TextField(verbose_name='Comentário', null=True, blank=True)
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE, verbose_name="Edital")

    def get_cpf_formatted(self):
        cpf = self.cpf
        if len(self.cpf) == 11:
            cpf = "{0}.{1}.{2}-{3}".format(self.cpf[0:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:-1])
        return cpf

    def get_point(self):
        return getPoints(self)

    def __str__(self):
        return str(self.nome_completo)
