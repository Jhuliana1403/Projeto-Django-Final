# Generated by Django 5.1.6 on 2025-02-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_transporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transporte',
            name='coleta',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
