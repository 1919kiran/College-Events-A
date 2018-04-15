# Generated by Django 2.0.3 on 2018-04-15 10:49

import datetime
from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_auto_20180415_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 15, 16, 19, 47, 584191)),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, height_field='300', null=True, upload_to=events.models.upload_location, width_field='400'),
        ),
    ]
