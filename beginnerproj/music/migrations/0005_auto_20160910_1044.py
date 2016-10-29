# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_song_song_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_upload',
            field=models.CharField(max_length=500),
        ),
    ]
