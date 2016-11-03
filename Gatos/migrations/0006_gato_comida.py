# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gatos', '0005_comida'),
    ]

    operations = [
        migrations.AddField(
            model_name='gato',
            name='comida',
            field=models.ForeignKey(related_name='gato_comida', default=1, to='Gatos.Comida'),
            preserve_default=False,
        ),
    ]
