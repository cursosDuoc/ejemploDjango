# Generated by Django 3.1.1 on 2020-10-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppersona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TarjetaJunaeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroTarjeta', models.TextField(max_length=12)),
                ('montoDisponible', models.IntegerField()),
                ('rut', models.TextField(max_length=9)),
                ('clave', models.TextField(max_length=8)),
            ],
        ),
    ]