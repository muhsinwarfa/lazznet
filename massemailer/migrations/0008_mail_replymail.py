# Generated by Django 2.2.5 on 2019-09-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('massemailer', '0007_mail_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='replymail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]