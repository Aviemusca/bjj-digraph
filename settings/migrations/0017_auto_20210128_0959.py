# Generated by Django 3.1.3 on 2021-01-28 09:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0016_auto_20210108_1014"),
    ]

    operations = [
        migrations.AddField(
            model_name="defaultnodesettings",
            name="level",
            field=models.PositiveSmallIntegerField(
                blank=True,
                default=0,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(16),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="defaultnodesettings",
            name="node_type",
            field=models.CharField(
                choices=[
                    ("score-entry-user", "score-entry-user"),
                    ("score-entry-opponent", "score-entry-opponent"),
                    ("score-position-user", "score-position-user"),
                    ("score-position-opponent", "score-position-opponent"),
                    ("score-submission-user", "score-submission-user"),
                    ("score-submission-opponent", "score-submission-opponent"),
                    ("score-transition-user", "score-transition-user"),
                    ("score-transition-opponent", "score-transition-opponent"),
                    ("score-grip-user", "score-grip-user"),
                    ("score-grip-opponent", "score-grip-opponent"),
                    ("score-sweep-user", "score-sweep-user"),
                    ("score-sweep-opponent", "score-sweep-opponent"),
                    ("score-action-user", "score-action-user"),
                    ("score-action-opponent", "score-action-opponent"),
                    ("meta-comment", "meta-comment"),
                    ("meta-text", "meta-text"),
                ],
                default="",
                max_length=128,
            ),
        ),
    ]
