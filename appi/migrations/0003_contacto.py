# Generated by Django 4.1.3 on 2022-11-26 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appi', '0002_orden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=400)),
                ('email', models.CharField(max_length=400)),
                ('numero', models.CharField(max_length=400)),
                ('mensaje', models.CharField(max_length=400)),
            ],
        ),
    ]