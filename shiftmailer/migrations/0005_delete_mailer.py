# Generated by Django 4.0.3 on 2022-03-16 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shiftmailer', '0004_location_to_facility'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mailer',
        ),
    ]
