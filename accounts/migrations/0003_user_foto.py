# Generated by Django 5.0.6 on 2024-07-17 02:20

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_apellido_alter_user_cedula_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_to),
        ),
    ]
