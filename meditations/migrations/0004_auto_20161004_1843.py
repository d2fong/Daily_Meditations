# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditations', '0003_auto_20161004_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meditation',
            name='category',
            field=models.CharField(max_length=40, choices=[('stoicism', 'stoicism')]),
        ),
    ]
