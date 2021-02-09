# Generated by Django 3.1.3 on 2021-01-07 13:45

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0010_auto_20210107_1335"),
    ]

    operations = [
        migrations.CreateModel(
            name="DefaultNodeSettings",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "node_type",
                    models.CharField(
                        choices=[
                            ("score-entry-user", "score-entry-user"),
                            ("score-entry-opponent", "score-entry-opponent"),
                            ("score-position-user", "score-position-user"),
                            ("score-position-opponent", "score-position-opponent"),
                            ("score-guardpass-user", "score-guardpass-user"),
                            ("score-guardpass-opponent", "score-guardpass-opponent"),
                            ("score-guardpull-user", "score-guardpull-user"),
                            ("score-guardpull-opponent", "score-guardpull-opponent"),
                            ("score-submission-user", "score-submission-user"),
                            ("score-submission-opponent", "score-submission-opponent"),
                            ("score-takedown-user", "score-takedown-user"),
                            ("score-takedown-opponent", "score-takedown-opponent"),
                            ("score-sweep-user", "score-sweep-user"),
                            ("score-sweep-opponent", "score-sweep-opponent"),
                            ("score-transition-user", "score-transition-user"),
                            ("score-transition-opponent", "score-transition-opponent"),
                            ("meta-comment", "meta-comment"),
                            ("meta-text", "meta-text"),
                        ],
                        default="",
                        max_length=128,
                    ),
                ),
                ("shape_id", models.CharField(default="#square", max_length=64)),
                ("type_text", models.CharField(default="", max_length=64)),
                (
                    "fill",
                    colorfield.fields.ColorField(default="#ad560e", max_length=18),
                ),
                ("fill_opacity", models.FloatField(default=1.0)),
                (
                    "stroke",
                    colorfield.fields.ColorField(default="#333333", max_length=18),
                ),
                ("stroke_opacity", models.FloatField(default=1.0)),
                ("stroke_width", models.PositiveSmallIntegerField(default=2)),
                (
                    "settings",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="settings.settings",
                    ),
                ),
            ],
            options={
                "verbose_name": "Default Node Settings",
            },
        ),
        migrations.DeleteModel(
            name="NodeSettings",
        ),
        migrations.AddField(
            model_name="gamenodesettings",
            name="node_type",
            field=models.CharField(
                choices=[
                    ("score-entry-user", "score-entry-user"),
                    ("score-entry-opponent", "score-entry-opponent"),
                    ("score-position-user", "score-position-user"),
                    ("score-position-opponent", "score-position-opponent"),
                    ("score-guardpass-user", "score-guardpass-user"),
                    ("score-guardpass-opponent", "score-guardpass-opponent"),
                    ("score-guardpull-user", "score-guardpull-user"),
                    ("score-guardpull-opponent", "score-guardpull-opponent"),
                    ("score-submission-user", "score-submission-user"),
                    ("score-submission-opponent", "score-submission-opponent"),
                    ("score-takedown-user", "score-takedown-user"),
                    ("score-takedown-opponent", "score-takedown-opponent"),
                    ("score-sweep-user", "score-sweep-user"),
                    ("score-sweep-opponent", "score-sweep-opponent"),
                    ("score-transition-user", "score-transition-user"),
                    ("score-transition-opponent", "score-transition-opponent"),
                    ("meta-comment", "meta-comment"),
                    ("meta-text", "meta-text"),
                ],
                default="",
                max_length=128,
            ),
        ),
        migrations.AddField(
            model_name="metanodesettings",
            name="node_type",
            field=models.CharField(
                choices=[
                    ("score-entry-user", "score-entry-user"),
                    ("score-entry-opponent", "score-entry-opponent"),
                    ("score-position-user", "score-position-user"),
                    ("score-position-opponent", "score-position-opponent"),
                    ("score-guardpass-user", "score-guardpass-user"),
                    ("score-guardpass-opponent", "score-guardpass-opponent"),
                    ("score-guardpull-user", "score-guardpull-user"),
                    ("score-guardpull-opponent", "score-guardpull-opponent"),
                    ("score-submission-user", "score-submission-user"),
                    ("score-submission-opponent", "score-submission-opponent"),
                    ("score-takedown-user", "score-takedown-user"),
                    ("score-takedown-opponent", "score-takedown-opponent"),
                    ("score-sweep-user", "score-sweep-user"),
                    ("score-sweep-opponent", "score-sweep-opponent"),
                    ("score-transition-user", "score-transition-user"),
                    ("score-transition-opponent", "score-transition-opponent"),
                    ("meta-comment", "meta-comment"),
                    ("meta-text", "meta-text"),
                ],
                default="",
                max_length=128,
            ),
        ),
    ]
