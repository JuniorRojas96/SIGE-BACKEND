# Generated by Django 5.0.3 on 2024-03-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0002_remove_alumno_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, null=True),
        ),
    ]
