# Generated by Django 2.0.3 on 2018-04-11 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_auto_20180411_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 11, 23, 1, 11, 956884)),
        ),
    ]