# Generated by Django 2.0.3 on 2018-04-05 22:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0039_auto_20180406_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 6, 3, 34, 50, 134839)),
        ),
    ]
