# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-08-31 08:08
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classify',
            options={'ordering': ['-reorder'], 'verbose_name': '商品分类', 'verbose_name_plural': '商品分类'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-reorder'], 'verbose_name': '商品标签', 'verbose_name_plural': '商品标签'},
        ),
        migrations.AlterField(
            model_name='classify',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='mall.Classify'),
        ),
        migrations.AlterField(
            model_name='product',
            name='classes',
            field=models.ManyToManyField(blank=True, null=True, related_name='classes', to='mall.Classify', verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='商品描述'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='mall.Tag', verbose_name='标签'),
        ),
    ]
