# Generated by Django 2.0.5 on 2019-07-18 22:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0002_add_greek_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flatpagetranslation",
            name="language",
            field=models.CharField(
                choices=[
                    ("en", "English"),
                    ("de", "German"),
                    ("fr", "French"),
                    ("el", "Greek"),
                    ("hu", "Hungarian"),
                    ("sv", "Swedish"),
                    ("pt", "Portuguese"),
                    ("tr", "Turkish"),
                ],
                max_length=20,
                verbose_name="language",
            ),
        ),
    ]
