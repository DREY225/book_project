# Generated by Django 4.2.5 on 2023-09-22 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phome', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
                ('country', models.CharField(choices=[('CI', 'Ivory Coast'), ('SN', 'Senegal'), ('ML', 'Mali'), ('TG', 'Togo'), ('BF', 'Burkina Faso')], max_length=2)),
            ],
        ),
    ]