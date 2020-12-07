# Generated by Django 3.1.3 on 2020-12-07 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0002_nodesettings_transition"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="gamenodesettings",
            unique_together={("game_type", "game_subtype")},
        ),
        migrations.CreateModel(
            name="Settings",
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
                (
                    "node_settings",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="settings.nodesettings",
                    ),
                ),
                (
                    "site_settings",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="settings.sitesettings",
                    ),
                ),
            ],
            options={
                "verbose_name": "Settings",
                "verbose_name_plural": "Settings",
            },
        ),
    ]
