# Generated by Django 4.1 on 2022-11-02 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curhat', '0001_initial'),
        ('curhat_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curhatadmin',
            name='curhat_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='curhat.curhatdong'),
        ),
    ]
