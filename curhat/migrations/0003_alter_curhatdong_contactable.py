from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curhat', '0002_rename_descriprion_curhatdong_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curhatdong',
            name='contactable',
            field=models.CharField(max_length=2),
        ),
    ]
