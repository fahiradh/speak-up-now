# Generated by Django 4.1 on 2022-11-01 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('curhat_admin', '0006_remove_curhatadmin_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='curhatadmin',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]