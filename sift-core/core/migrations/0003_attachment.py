# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-04 01:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160201_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_file', models.FileField(upload_to='', verbose_name='attachment')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Response')),
            ],
        ),
    ]
