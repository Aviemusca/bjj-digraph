# Generated by Django 3.1.3 on 2021-01-07 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0014_auto_20210107_1439"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="defaultnodesettings",
            unique_together={("settings", "node_type")},
        ),
    ]
