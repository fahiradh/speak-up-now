# Generated by Django 4.1 on 2022-12-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengguna',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]