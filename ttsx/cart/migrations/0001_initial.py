# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
        ('goods', '0002_auto_20170707_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(default=1)),
                ('goods', models.ForeignKey(to='goods.GoodsInfo')),
                ('user', models.ForeignKey(to='df_user.UserInfo')),
            ],
        ),
    ]
