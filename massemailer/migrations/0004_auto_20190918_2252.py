# Generated by Django 2.2.5 on 2019-09-18 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('massemailer', '0003_auto_20190918_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='receiver',
            field=models.CharField(max_length=100),
        ),
    ]
