# Generated by Django 3.1.3 on 2021-07-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
                ('add', models.TextField(null=True)),
                ('consulting', models.BooleanField(default=False)),
            ],
        ),
    ]
