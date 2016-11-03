# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gatos', '0002_gato_comida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gato',
            name='comida',
        ),
        migrations.DeleteModel(
            name='Comida',
        ),
        migrations.DeleteModel(
            name='Gato',
        ),
    ]
