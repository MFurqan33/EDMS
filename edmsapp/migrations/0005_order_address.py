# Generated by Django 3.2 on 2023-06-03 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edmsapp', '0004_auto_20230528_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
