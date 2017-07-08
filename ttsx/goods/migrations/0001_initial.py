# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('pic', models.ImageField(upload_to=b'goods/')),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('click', models.IntegerField()),
                ('unit', models.CharField(max_length=10)),
                ('isDelete', models.BooleanField(default=False)),
                ('subtitle', models.CharField(max_length=200)),
                ('store', models.IntegerField(default=100)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20)),
                ('isdelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodinfo',
            name='type',
            field=models.ForeignKey(to='goods.GoodsType'),
        ),
    ]
