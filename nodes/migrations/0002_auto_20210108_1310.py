# Generated by Django 3.1.3 on 2021-01-08 13:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edges', '0001_initial'),
        ('nodes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreNode',
            fields=[
                ('node_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nodes.node')),
                ('description', models.TextField(blank=True, default='')),
                ('comment', models.TextField(blank=True, default='')),
                ('effectiveness', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)])),
                ('priority', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)])),
                ('proficiency', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'verbose_name': 'Score Node',
                'verbose_name_plural': 'Score Nodes',
            },
            bases=('nodes.node',),
        ),
        migrations.RemoveField(
            model_name='metanode',
            name='meta_type',
        ),
        migrations.AddField(
            model_name='node',
            name='node_type',
            field=models.CharField(choices=[('score-entry-user', 'score-entry-user'), ('score-entry-opponent', 'score-entry-opponent'), ('score-position-user', 'score-position-user'), ('score-position-opponent', 'score-position-opponent'), ('score-guardpass-user', 'score-guardpass-user'), ('score-guardpass-opponent', 'score-guardpass-opponent'), ('score-guardpull-user', 'score-guardpull-user'), ('score-guardpull-opponent', 'score-guardpull-opponent'), ('score-submission-user', 'score-submission-user'), ('score-submission-opponent', 'score-submission-opponent'), ('score-takedown-user', 'score-takedown-user'), ('score-takedown-opponent', 'score-takedown-opponent'), ('score-sweep-user', 'score-sweep-user'), ('score-sweep-opponent', 'score-sweep-opponent'), ('score-transition-user', 'score-transition-user'), ('score-transition-opponent', 'score-transition-opponent'), ('meta-comment', 'meta-comment'), ('meta-text', 'meta-text')], default='score-position-user', max_length=128),
        ),
        migrations.DeleteModel(
            name='GameNode',
        ),
    ]
