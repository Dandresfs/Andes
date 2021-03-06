# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import acceso.models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0011_auto_20150904_1547'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acceso', '0013_auto_20151208_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargaMasivaApoyo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('excel', models.FileField(upload_to=acceso.models.masivo)),
                ('archivo', models.FileField(upload_to=acceso.models.masivo)),
                ('region', models.ForeignKey(to='region.Region')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
