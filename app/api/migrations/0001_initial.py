# Generated by Django 5.0.3 on 2024-06-30 23:35

import api.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sorting', models.FloatField(default=0.1)),
                ('public', models.BooleanField(default=True)),
                ('show_to_authenticated', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sorting', models.FloatField(default=0.1)),
                ('public', models.BooleanField(default=True)),
                ('show_to_authenticated', models.BooleanField(default=True)),
                ('picture', models.ImageField(upload_to=api.models.upload_picture)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('tags', models.ManyToManyField(blank=True, to='api.tagging')),
            ],
            options={
                'ordering': ['sorting'],
            },
        ),
        migrations.CreateModel(
            name='AssetJson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sorting', models.FloatField(default=0.1)),
                ('public', models.BooleanField(default=True)),
                ('show_to_authenticated', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('json', models.JSONField(blank=True, default=dict, null=True)),
                ('members', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='api.tagging')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sorting', models.FloatField(default=0.1)),
                ('public', models.BooleanField(default=True)),
                ('show_to_authenticated', models.BooleanField(default=True)),
                ('text', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('tags', models.ManyToManyField(blank=True, to='api.tagging')),
            ],
            options={
                'ordering': ['sorting'],
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sorting', models.FloatField(default=0.1)),
                ('public', models.BooleanField(default=True)),
                ('show_to_authenticated', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('links', models.JSONField(blank=True, default=list, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.picture')),
                ('tags', models.ManyToManyField(blank=True, to='api.tagging')),
                ('texts', models.ManyToManyField(blank=True, to='api.text')),
            ],
            options={
                'ordering': ['sorting'],
            },
        ),
    ]