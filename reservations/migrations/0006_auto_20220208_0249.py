# Generated by Django 3.2 on 2022-02-08 02:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_auto_20220206_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservations',
            name='id',
        ),
        migrations.AddField(
            model_name='reservations',
            name='reservation_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
