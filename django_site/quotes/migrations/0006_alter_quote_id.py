# Generated by Django 5.1.2 on 2024-10-31 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_alter_quote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
