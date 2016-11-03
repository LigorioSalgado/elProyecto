# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gato',
            name='comida',
            field=models.ForeignKey(related_name='gato_comida', default='', to='Gatos.Comida'),
            preserve_default=False,
        ),
    ]
