# Generated by Django 3.2.8 on 2022-05-06 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerapp', '0005_partner_feedback_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Four_wheeler',
            fields=[
                ('assign_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50, verbose_name='Name')),
                ('price', models.CharField(db_column='price', max_length=50, verbose_name='Price')),
            ],
            options={
                'db_table': 'Four_wheeler',
            },
        ),
    ]