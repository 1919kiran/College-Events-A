# Generated by Django 2.0.3 on 2018-04-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logins', '0009_auto_20180414_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupdata',
            name='phone_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]