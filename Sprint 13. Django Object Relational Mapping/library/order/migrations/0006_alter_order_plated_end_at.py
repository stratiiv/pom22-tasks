# Generated by Django 4.1 on 2022-08-27 12:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_order_end_at_alter_order_plated_end_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='plated_end_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 10, 12, 6, 5, 949458, tzinfo=datetime.timezone.utc)),
        ),
    ]
