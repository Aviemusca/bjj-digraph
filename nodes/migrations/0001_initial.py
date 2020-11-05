# Generated by Django 3.1.3 on 2020-11-05 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Node",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                (
                    "node_type",
                    models.CharField(
                        choices=[
                            ("position", "position"),
                            ("submission", "submission"),
                            ("entry", "entry"),
                            ("transition", "transition"),
                            ("sweep", "sweep"),
                            ("conditional", "conditional"),
                        ],
                        default="",
                        max_length=50,
                    ),
                ),
                ("description", models.TextField(default="")),
                ("comment", models.TextField(default="")),
                ("effectiveness", models.IntegerField(default=50)),
                ("priority", models.IntegerField(default=50)),
                ("proficiency", models.IntegerField(default=50)),
                ("position_x", models.FloatField(default=100)),
                ("position_y", models.FloatField(default=100)),
            ],
        ),
    ]
