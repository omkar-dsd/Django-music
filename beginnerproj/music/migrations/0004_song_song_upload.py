# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20160825_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_upload',
            field=models.FileField(default=datetime.datetime(2016, 8, 28, 14, 28, 25, 943807, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]
