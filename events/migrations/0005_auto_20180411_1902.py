# Generated by Django 2.0.3 on 2018-04-11 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20180409_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 11, 19, 2, 47, 100196)),
        ),
    ]