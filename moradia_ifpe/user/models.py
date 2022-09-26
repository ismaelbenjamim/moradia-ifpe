from django.contrib.auth.models import AbstractUser
from django.db import models


TYPES_CAMPUS = (
    ("0", "Barreiros"),
    ("1", "Belo Jardim"),
    ("2", "Vitória de Santo Antão")
)


class User(AbstractUser):
    TYPES_PERMISSION = (
        ("0", "Usuário"),
        ("1", "Administrador"),
    )
    first_name = models.CharField("Nome", max_length=150, blank=True)
    last_name = models.CharField("Sobrenome", max_length=150, blank=True)
    photo = models.ImageField(verbose_name="Photo", null=True, blank=True)
    campus = models.CharField("Campus", choices=TYPES_CAMPUS, max_length=50, null=True, blank=True)
    permission = models.CharField("Permissão", choices=TYPES_PERMISSION, max_length=50, default=0)

    def get_name(self):
        if self.first_name and not self.last_name:
            return f"{self.first_name}"
        elif self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.username
