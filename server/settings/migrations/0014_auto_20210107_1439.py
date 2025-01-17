# Generated by Django 3.1.3 on 2021-01-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0013_auto_20210107_1438"),
    ]

    operations = [
        migrations.AlterField(
            model_name="defaultnodesettings",
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
        migrations.AlterField(
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
        migrations.AlterField(
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
