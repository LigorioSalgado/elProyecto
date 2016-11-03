# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gatos', '0004_gato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=25)),
                ('compra', models.DateField(auto_now_add=True)),
                ('caducidad', models.DateField()),
            ],
        ),
    ]
