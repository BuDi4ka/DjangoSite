# Generated by Django 5.1.2 on 2024-10-30 15:18

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('born_date', models.DateField(blank=True, null=True)),
                ('born_location', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('quote', models.TextField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.author')),
            ],
        ),
    ]
