# Generated by Django 3.1.3 on 2020-11-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('courses_category', '0001_initial'),
        ('courses', '0014_auto_20201119_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(to='courses_category.Category'),
        ),
    ]
