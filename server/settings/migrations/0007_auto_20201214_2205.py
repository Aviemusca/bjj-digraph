# Generated by Django 3.1.3 on 2020-12-14 22:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0006_auto_20201214_2203"),
    ]

    operations = [
        migrations.AddField(
            model_name="nodesettings",
            name="node_subtype",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("position", "position"),
                        ("submission", "submission"),
                        ("entry", "entry"),
                        ("transition", "transition"),
                        ("sweep", "sweep"),
                        ("takedown", "takedown"),
                        ("guardPull", "guardPull"),
                        ("guardPass", "guardPass"),
                        ("user", "user"),
                        ("opponent", "opponent"),
                        ("comment", "comment"),
                        ("text", "text"),
                    ],
                    default="",
                    max_length=32,
                ),
                default=list,
                size=3,
            ),
        ),
        migrations.AlterField(
            model_name="nodesettings",
            name="node_type",
            field=models.CharField(
                choices=[("game", "game"), ("meta", "meta")], default="", max_length=16
            ),
        ),
    ]
