# Generated by Django 5.0.6 on 2024-05-13 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_car_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='owner',
        ),
    ]
