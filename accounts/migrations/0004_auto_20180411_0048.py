# Generated by Django 2.0.3 on 2018-04-10 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180411_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='events_related',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
    ]