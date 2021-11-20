# Generated by Django 3.1.3 on 2021-07-25 14:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0001_migrations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulting',
            name='tel',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\09\\[0-9]{9}')]),
        ),
    ]