# Generated by Django 3.1.7 on 2021-05-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electricity_accounting_app', '0002_auto_20210517_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='flat',
            field=models.IntegerField(default=0, verbose_name='Flat'),
            preserve_default=False,
        ),
    ]
