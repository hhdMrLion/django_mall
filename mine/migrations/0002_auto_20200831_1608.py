# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-08-31 08:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': '购物车', 'verbose_name_plural': '购物车'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': '商品评论', 'verbose_name_plural': '商品评论'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '订单管理', 'verbose_name_plural': '订单管理'},
        ),
    ]
