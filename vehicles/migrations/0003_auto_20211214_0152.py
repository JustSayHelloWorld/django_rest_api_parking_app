# Generated by Django 3.1.5 on 2021-12-14 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_auto_20211214_0041'),
        ('vehicles', '0002_auto_20211214_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='driver_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drivers.driver'),
        ),
    ]
