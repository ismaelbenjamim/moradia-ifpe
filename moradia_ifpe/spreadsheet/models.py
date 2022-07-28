import uuid as uuid
from django.db import models

class Campi(models.Model):
    uuid = models.UUIDField("UUID", default=uuid.uuid4, unique=True, primary_key=True)
    nome = models.CharField("Nome", max_length=200, unique=True)

    def __str__(self):
        return str(self.nome)

class SpreadSheet(models.Model):
    uuid = models.UUIDField("UUID", default=uuid.uuid4, unique=True, primary_key=True)
    campi = models.ForeignKey(Campi, on_delete=models.CASCADE, verbose_name="Campi")
    edital = models.CharField("Edital", max_length=200, blank=True, null=True)
    ano = models.CharField("Ano", max_length=4, blank=True, null=True)
    file = models.FileField("File", null=True, blank=True)
