# Generated by Django 4.2.5 on 2023-09-23 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'managed': True, 'verbose_name': 'auteur', 'verbose_name_plural': 'auteurs'},
        ),
        migrations.AlterModelTable(
            name='author',
            table='auteurs',
        ),
    ]