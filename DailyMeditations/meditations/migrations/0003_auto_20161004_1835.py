# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditations', '0002_auto_20161004_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meditation',
            name='category',
            field=models.CharField(choices=[('STOICISM', 'stoicism')], max_length=40),
        ),
    ]
