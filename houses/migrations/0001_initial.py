# Generated by Django 2.0.13 on 2019-03-07 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_owner', models.CharField(max_length=265)),
                ('address', models.CharField(max_length=255)),
                ('rent', models.PositiveIntegerField()),
                ('house_details', models.TextField()),
                ('house_pic', models.ImageField(blank=True, null=True, upload_to='houses')),
                ('rooms', models.PositiveIntegerField()),
                ('students', models.PositiveIntegerField()),
                ('bathrooms', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Both', 'Both')], default='0', max_length=20)),
                ('property_choice', models.CharField(choices=[('Apartment', 'Apartment'), ('Full House', 'Full House'), ('Rooms', 'Rooms')], default='2', max_length=20)),
                ('space_type', models.CharField(choices=[('Shared Room', 'Shared Room'), ('Private Room', 'Private Room'), ('Entire Space', 'Entire Space')], default='0', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
