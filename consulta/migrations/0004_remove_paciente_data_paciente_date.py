# Generated by Django 4.0.4 on 2022-05-19 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0003_paciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='data',
        ),
        migrations.AddField(
            model_name='paciente',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
