# Generated by Django 2.0.13 on 2019-03-05 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0014_remove_housemodel_house_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='housemodel',
            name='house_pic',
            field=models.ImageField(blank=True, null=True, upload_to='houses'),
        ),
    ]
