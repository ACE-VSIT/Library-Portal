# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('acelibraryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=200)),
                ('attendance_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EventNameDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('date_id', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='resources',
            name='category',
            field=models.CharField(default='ignore', max_length=30),
            preserve_default=False,
        ),
    ]
