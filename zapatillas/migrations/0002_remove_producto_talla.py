# Generated by Django 4.1.2 on 2023-06-29 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zapatillas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='talla',
        ),
    ]
