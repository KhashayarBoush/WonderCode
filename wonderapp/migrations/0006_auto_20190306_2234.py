# Generated by Django 2.1.7 on 2019-03-06 22:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wonderapp', '0005_auto_20190306_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid3, primary_key=True, serialize=False, unique=True),
        ),
    ]
