# Generated by Django 5.0.6 on 2024-05-13 18:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2020)]),
        ),
    ]