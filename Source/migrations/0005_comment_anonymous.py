# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Source', '0004_auto_20160825_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
