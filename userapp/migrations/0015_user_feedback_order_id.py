# Generated by Django 3.2.8 on 2022-05-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0014_user_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_feedback',
            name='order_id',
            field=models.CharField(db_column='order_id', max_length=50, null=True, verbose_name='Order_id'),
        ),
    ]
