# Generated by Django 4.1 on 2022-10-31 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='laporan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('phone_num', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('case_name', models.CharField(max_length=30)),
                ('victim_name', models.CharField(max_length=60)),
                ('victim_description', models.CharField(max_length=2000)),
                ('crime_place', models.CharField(max_length=100)),
                ('chronology', models.TextField(max_length=5000)),
            ],
        ),
    ]
