# Generated by Django 4.1 on 2022-10-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curhatDong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('descriprion', models.CharField(max_length=520)),
                ('contactable', models.CharField(max_length=20)),
            ],
        ),
    ]