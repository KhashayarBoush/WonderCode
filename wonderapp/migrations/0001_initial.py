# Generated by Django 2.1.7 on 2019-03-06 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('Family', models.CharField(max_length=300)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Project', models.TextField(help_text='please write your projects about')),
            ],
        ),
    ]
