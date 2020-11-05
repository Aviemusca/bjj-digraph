# Generated by Django 3.1.3 on 2020-11-05 18:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("nodes", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="node",
            options={"verbose_name": "Node", "verbose_name_plural": "Nodes"},
        ),
        migrations.AddField(
            model_name="node",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
