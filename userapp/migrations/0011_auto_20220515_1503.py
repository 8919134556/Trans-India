# Generated by Django 3.2.8 on 2022-05-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0010_auto_20220515_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='lynk',
            name='cap_id',
            field=models.CharField(db_column='cap_id', max_length=50, null=True, verbose_name='Cap_id'),
        ),
        migrations.AddField(
            model_name='lynk',
            name='status',
            field=models.CharField(db_column='status', max_length=50, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='portor',
            name='cap_id',
            field=models.CharField(db_column='cap_id', max_length=50, null=True, verbose_name='Cap_id'),
        ),
        migrations.AddField(
            model_name='portor',
            name='status',
            field=models.CharField(db_column='status', max_length=50, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='rapido',
            name='cap_id',
            field=models.CharField(db_column='cap_id', max_length=50, null=True, verbose_name='Cap_id'),
        ),
        migrations.AddField(
            model_name='rapido',
            name='status',
            field=models.CharField(db_column='status', max_length=50, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='swiggy_genie',
            name='cap_id',
            field=models.CharField(db_column='cap_id', max_length=50, null=True, verbose_name='Cap_id'),
        ),
        migrations.AddField(
            model_name='swiggy_genie',
            name='status',
            field=models.CharField(db_column='status', max_length=50, null=True, verbose_name='Status'),
        ),
    ]
