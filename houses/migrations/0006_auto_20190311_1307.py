# Generated by Django 2.0.13 on 2019-03-11 11:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0005_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 11, 11, 6, 55, 670807, tzinfo=utc)),
        ),
    ]