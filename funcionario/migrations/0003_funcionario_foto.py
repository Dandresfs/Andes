# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0002_auto_20150903_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='foto',
            field=models.FileField(upload_to=b'Funcionarios/Foto/', blank=True),
        ),
    ]
