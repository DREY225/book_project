# Generated by Django 4.2.5 on 2023-09-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]