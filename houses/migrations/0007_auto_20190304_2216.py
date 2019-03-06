# Generated by Django 2.0.13 on 2019-03-04 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0006_auto_20190304_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemodel',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Both', 'Both')], default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='housemodel',
            name='property_choice',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('Full House', 'Full House'), ('Rooms', 'Rooms')], default='2', max_length=20),
        ),
        migrations.AlterField(
            model_name='housemodel',
            name='space_type',
            field=models.CharField(choices=[('Shared Room', 'Shared Room'), ('Private Room', 'Private Room'), ('Entire Space', 'Entire Space')], default='0', max_length=20),
        ),
    ]