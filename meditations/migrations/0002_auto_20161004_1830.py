# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meditation',
            name='category',
            field=models.IntegerField(choices=[('STOICISM', 'stoicism')]),
        ),
    ]
