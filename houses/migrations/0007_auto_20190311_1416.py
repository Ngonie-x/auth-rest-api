# Generated by Django 2.0.13 on 2019-03-11 12:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0006_auto_20190311_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 11, 12, 16, 30, 678385, tzinfo=utc)),
        ),
    ]
