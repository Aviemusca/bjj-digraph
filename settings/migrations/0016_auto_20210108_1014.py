# Generated by Django 3.1.3 on 2021-01-08 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0015_auto_20210107_1446"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="metanodesettings",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="metanodesettings",
            name="settings",
        ),
        migrations.DeleteModel(
            name="GameNodeSettings",
        ),
        migrations.DeleteModel(
            name="MetaNodeSettings",
        ),
    ]
