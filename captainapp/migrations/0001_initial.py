# Generated by Django 3.2.8 on 2022-04-09 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Captain_Register',
            fields=[
                ('assign_id', models.AutoField(primary_key=True, serialize=False)),
                ('cap_name', models.CharField(db_column='cap_name', max_length=50, verbose_name='Cap_Name')),
                ('cap_phone', models.BigIntegerField(db_column='cap_phone', verbose_name='Cap_Phone')),
                ('cap_license', models.CharField(db_column='cap_license', max_length=50, verbose_name='Cap_License')),
                ('city', models.CharField(db_column='city', max_length=50, verbose_name='City')),
                ('vechicle', models.CharField(db_column='vechicle', max_length=50, verbose_name='Vechicle')),
                ('cap_email', models.EmailField(blank=True, db_column='cap_email', max_length=100, null=True, verbose_name='Cap_Email')),
                ('cap_pwd', models.CharField(db_column='cap_pwd', max_length=100, verbose_name='Cap_Password')),
                ('cap_image', models.FileField(db_column='cap_image', upload_to='Captain/Profile-image/', verbose_name='Cap_Image')),
                ('cap_vehicle_image', models.FileField(db_column='cap_vehicle_image', upload_to='Captain/Vehicle-image/', verbose_name='Cap_Vehicle_Image')),
                ('cap_driving_lic', models.FileField(db_column='cap_driving_lic', upload_to='Captain/Driving-image/', verbose_name='Cap_Driving_Lic')),
                ('status', models.CharField(db_column='status', max_length=50, null=True, verbose_name='Status')),
                ('datetime_created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'assign_details',
            },
        ),
    ]
