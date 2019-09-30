# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-09-15 21:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingparcelpost',
            name='receive_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Receive date'),
        ),
        migrations.AlterField(
            model_name='outgoingparcelpost',
            name='post_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Post date'),
        ),
    ]