# Generated by Django 2.2.5 on 2019-09-22 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('massemailer', '0009_auto_20190922_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapper',
            name='csvdump',
            field=models.TextField(default='insert website'),
        ),
    ]
