# Generated by Django 2.0.3 on 2018-04-15 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0023_auto_20180416_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 16, 0, 41, 32, 227258)),
        ),
    ]
