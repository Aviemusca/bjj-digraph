# Generated by Django 3.1.3 on 2020-12-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_settings", "0005_auto_20201208_1935"),
    ]

    operations = [
        migrations.AddField(
            model_name="usergamenodesettings",
            name="type_text",
            field=models.CharField(default="", max_length=64),
        ),
        migrations.AddField(
            model_name="usermetanodesettings",
            name="type_text",
            field=models.CharField(default="", max_length=64),
        ),
    ]
