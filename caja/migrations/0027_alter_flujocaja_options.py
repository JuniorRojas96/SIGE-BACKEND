# Generated by Django 5.0.6 on 2024-06-22 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0026_alter_flujocaja_entrada_alter_flujocaja_salida'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flujocaja',
            options={'ordering': ['-fecha']},
        ),
    ]
