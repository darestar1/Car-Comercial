# Generated by Django 4.2.4 on 2023-08-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_photo_5',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/d'),
        ),
    ]
