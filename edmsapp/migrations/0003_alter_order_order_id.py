# Generated by Django 3.2 on 2023-05-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edmsapp', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=100),
        ),
    ]
