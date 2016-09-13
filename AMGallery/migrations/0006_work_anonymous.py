# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AMGallery', '0005_comment_anonymous'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
