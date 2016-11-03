# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gatos', '0003_auto_20161103_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField(default=0, blank=True)),
                ('callejero', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Gato',
                'verbose_name_plural': 'Gatos',
            },
        ),
    ]
