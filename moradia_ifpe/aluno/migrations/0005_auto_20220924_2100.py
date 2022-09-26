# Generated by Django 3.2.14 on 2022-09-24 21:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0004_aluno_edital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='ano',
            field=models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Ano'),
        ),
        migrations.AlterField(
            model_name='edital',
            name='periodo',
            field=models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Período'),
        ),
    ]