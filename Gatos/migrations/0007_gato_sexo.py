# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gatos', '0006_gato_comida'),
    ]

    operations = [
        migrations.AddField(
            model_name='gato',
            name='sexo',
            field=models.CharField(default='M', max_length=10, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')]),
            preserve_default=False,
        ),
    ]
