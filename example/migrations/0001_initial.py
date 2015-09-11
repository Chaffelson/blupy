# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.IntegerField(default=1, help_text='Set both x and y and hit save for celery to calculate the result')),
                ('y', models.IntegerField(default=1, help_text='Set both x and y and hit save for celery to calculate the result')),
                ('result', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
