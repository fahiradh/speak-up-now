

#Generated by Django 4.1 on 2022-11-02 14:46


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curhat_admin', '0002_curhatadmin_curhat_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curhatadmin',
            name='user',
        ),
    ]
