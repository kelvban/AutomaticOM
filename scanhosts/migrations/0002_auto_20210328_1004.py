# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='browseinfo',
            old_name='useragent',
            new_name='user_agent',
        ),
        migrations.RenameField(
            model_name='browseinfo',
            old_name='userip',
            new_name='user_ip',
        ),
    ]
