# Generated by Django 3.2.9 on 2021-12-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('consulting', '0003_auto_20210725_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulting',
            name='tel',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
