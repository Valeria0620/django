# Generated by Django 3.2.4 on 2021-06-08 14:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210608_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 8, 17, 46, 41, 32626, tzinfo=utc), verbose_name='Published date'),
        ),
    ]
