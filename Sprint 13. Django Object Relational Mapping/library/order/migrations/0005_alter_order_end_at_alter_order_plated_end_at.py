# Generated by Django 4.1 on 2022-08-27 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='plated_end_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 10, 12, 4, 19, 329616, tzinfo=datetime.timezone.utc)),
        ),
    ]
