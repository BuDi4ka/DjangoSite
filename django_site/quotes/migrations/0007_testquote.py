# Generated by Django 5.1.2 on 2024-10-31 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0006_alter_quote_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestQuote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quote', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.author')),
            ],
        ),
    ]