# Generated by Django 3.2 on 2022-02-08 21:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0009_alter_reservations_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='phone_number',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
