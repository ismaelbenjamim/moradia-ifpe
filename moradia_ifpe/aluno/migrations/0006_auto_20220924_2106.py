# Generated by Django 3.2.14 on 2022-09-24 21:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0005_auto_20220924_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='edital',
            name='data_abertura',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de abertura'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='edital',
            unique_together={('ano', 'periodo', 'data_abertura')},
        ),
    ]
