# Generated by Django 3.1.7 on 2021-06-14 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electricity_accounting_app', '0004_auto_20210614_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='renter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='electricity_accounting_app.renter'),
            preserve_default=False,
        ),
    ]