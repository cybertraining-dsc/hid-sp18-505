# Generated by Django 2.0.2 on 2018-02-14 04:48

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appclimate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='raingage',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='raingage',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='raingage',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]