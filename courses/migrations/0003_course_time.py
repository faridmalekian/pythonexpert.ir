# Generated by Django 3.1.3 on 2020-11-12 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20201111_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
