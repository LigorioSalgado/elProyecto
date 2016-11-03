# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50)),
                ('caducidad', models.DateField()),
                ('creada', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('edad', models.CharField(default=0, max_length=2, blank=True)),
                ('cache', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Gato',
                'verbose_name_plural': 'Gatos',
            },
        ),
    ]
