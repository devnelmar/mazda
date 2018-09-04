# Generated by Django 2.1.1 on 2018-09-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('edad', models.IntegerField()),
                ('identificacion', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=12)),
            ],
        ),
    ]