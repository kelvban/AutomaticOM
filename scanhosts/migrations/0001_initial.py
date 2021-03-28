# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrowseInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('useragent', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u7528\u6237\u6d4f\u89c8\u5668agent\u4fe1\u606f')),
            ],
            options={
                'db_table': 'browse_info',
                'verbose_name': '\u7528\u6237\u6d4f\u89c8\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u7528\u6237\u6d4f\u89c8\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='UserIPInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(default=b'', max_length=40, null=True, verbose_name='ip\u5730\u5740')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'db_table': 'user_ip_info',
                'verbose_name': '\u7528\u6237\u8bbf\u95ee\u5730\u5740\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u7528\u6237\u8bbf\u95ee\u5730\u5740\u4fe1\u606f\u8868',
            },
        ),
        migrations.AddField(
            model_name='browseinfo',
            name='userip',
            field=models.ForeignKey(to='scanhosts.UserIPInfo'),
        ),
    ]
