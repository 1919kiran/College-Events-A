# Generated by Django 2.0.3 on 2018-04-05 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0030_auto_20180404_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contact',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 6, 1, 21, 18, 193240)),
        ),
    ]