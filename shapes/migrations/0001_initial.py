# Generated by Django 3.1.3 on 2020-12-08 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeShape',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('shape_id', models.CharField(default='#square', max_length=100)),
                ('fill', models.CharField(default='#DDDDDD', max_length=20)),
                ('opacity', models.CharField(default='100', max_length=3)),
                ('stroke', models.CharField(default='#333333', max_length=20)),
                ('stroke_width', models.CharField(default='2', max_length=3)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='node_shapes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameNodeShape',
            fields=[
                ('nodeshape_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shapes.nodeshape')),
                ('game_type', models.CharField(choices=[], default='position', max_length=50)),
                ('game_subtype', models.CharField(choices=[], default='user', max_length=50)),
            ],
            options={
                'verbose_name': 'Game Node Shape',
                'verbose_name_plural': 'Game Node Shapes',
            },
            bases=('shapes.nodeshape',),
        ),
        migrations.CreateModel(
            name='MetaNodeShape',
            fields=[
                ('nodeshape_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shapes.nodeshape')),
                ('meta_type', models.CharField(choices=[], default='comment', max_length=50)),
            ],
            options={
                'verbose_name': 'Meta Node Shape',
                'verbose_name_plural': 'Meta Node Shapes',
            },
            bases=('shapes.nodeshape',),
        ),
    ]
