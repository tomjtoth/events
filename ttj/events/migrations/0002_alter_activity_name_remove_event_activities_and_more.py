# Generated by Django 4.2.6 on 2023-10-28 17:04

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(default='something', max_length=100),
        ),
        migrations.RemoveField(
            model_name='event',
            name='activities',
        ),
        migrations.AlterField(
            model_name='event',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=3600)),
        ),
        migrations.RemoveField(
            model_name='event',
            name='participants',
        ),
        migrations.AddField(
            model_name='event',
            name='activities',
            field=models.ManyToManyField(to='events.activity'),
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
