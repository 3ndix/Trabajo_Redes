# Generated by Django 3.0.5 on 2020-04-25 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rut',
            field=models.CharField(max_length=25),
        ),
    ]
