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
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('goods', models.ForeignKey(to='goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMain',
            fields=[
                ('orderid', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('count', models.DecimalField(max_digits=8, decimal_places=2)),
                ('user', models.ForeignKey(to='df_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(to='order.OrderMain'),
        ),
    ]
