# Generated by Django 2.0.13 on 2019-03-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0010_auto_20190305_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemodel',
            name='house_pic',
            field=models.ImageField(blank=True, default='pexels-photo-670061.jpeg', upload_to='houses'),
        ),
    ]
