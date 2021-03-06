# Generated by Django 3.2.8 on 2022-05-02 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerapp', '0003_auto_20220502_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner_feedback',
            name='email',
            field=models.EmailField(blank=True, db_column='email', max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='partner_feedback',
            name='name',
            field=models.CharField(db_column='Name', max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='partner_feedback',
            name='phone',
            field=models.BigIntegerField(db_column='phone', null=True, verbose_name='Phone'),
        ),
    ]
