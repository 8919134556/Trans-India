# Generated by Django 3.2.8 on 2022-04-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Two_wheeler',
            fields=[
                ('assign_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', default='Two-wheeler', max_length=50, verbose_name='Name')),
                ('price', models.CharField(db_column='price', default='5', max_length=50, verbose_name='Price')),
            ],
            options={
                'db_table': 'Two_wheeler',
            },
        ),
    ]
