# Generated by Django 3.2.8 on 2022-05-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerapp', '0006_four_wheeler'),
    ]

    operations = [
        migrations.AddField(
            model_name='four_wheeler',
            name='image',
            field=models.FileField(db_column='image', default='null', upload_to='demo/', verbose_name='Image'),
        ),
    ]