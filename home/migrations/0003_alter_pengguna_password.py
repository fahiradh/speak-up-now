# Generated by Django 4.1 on 2022-12-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_pengguna_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengguna',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
