# Generated by Django 3.1.5 on 2021-12-14 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0002_auto_20211214_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(editable=False, max_length=20)),
                ('model', models.CharField(editable=False, max_length=20)),
                ('plate_number', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('driver_id', models.ForeignKey(default='no driver assigned', on_delete=django.db.models.deletion.SET_DEFAULT, to='drivers.driver')),
            ],
        ),
    ]
