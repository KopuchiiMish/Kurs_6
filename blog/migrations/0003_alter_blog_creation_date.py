# Generated by Django 4.2.6 on 2023-11-01 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 1, 18, 28, 38, 360410), verbose_name='Дата создания'),
        ),
    ]
