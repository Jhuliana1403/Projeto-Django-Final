# Generated by Django 5.1.6 on 2025-02-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_transporte_ativo_transporte_data_chegada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transporte',
            name='data_envio',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
