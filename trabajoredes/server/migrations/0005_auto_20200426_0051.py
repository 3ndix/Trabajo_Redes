# Generated by Django 3.0.5 on 2020-04-26 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_auto_20200426_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='comprut',
            field=models.BooleanField(verbose_name=True),
        ),
    ]