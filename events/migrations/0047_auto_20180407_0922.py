# Generated by Django 2.0.3 on 2018-04-07 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0046_auto_20180406_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 9, 22, 36, 956044)),
        ),
    ]