# Generated by Django 5.1.2 on 2024-11-04 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0010_tag_quote_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestQuote',
        ),
    ]
