# Generated by Django 3.1.3 on 2020-11-13 04:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('courses', '0006_auto_20201112_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
