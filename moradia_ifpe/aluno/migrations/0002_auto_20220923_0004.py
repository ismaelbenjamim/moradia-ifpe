# Generated by Django 3.2.14 on 2022-09-23 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='beneficiario_bolsa_social',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Beneficiário'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='curso',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='orientacao_sexual',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Orientação sexual'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='origem_escolar',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Origem escolar'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='passo',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Passo'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='raca',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Raça'),
        ),
        migrations.DeleteModel(
            name='Beneficiario',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='OrientacaoSexual',
        ),
        migrations.DeleteModel(
            name='OrigemEscolar',
        ),
        migrations.DeleteModel(
            name='Passo',
        ),
        migrations.DeleteModel(
            name='Raca',
        ),
    ]