# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0035_delete_topics_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='facility',
            field=models.ForeignKey(verbose_name='facility', to='organizations.Facility'),
        ),
    ]