# Generated by Django 3.1.3 on 2020-11-20 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_category', '0001_initial'),
        ('account', '0006_auto_20201119_0526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='your_expertise',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='your_expertise',
            field=models.ManyToManyField(to='courses_category.Category'),
        ),
    ]
