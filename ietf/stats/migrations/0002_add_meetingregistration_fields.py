# Generated by Django 2.0.13 on 2020-06-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingregistration',
            name='reg_type',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='meetingregistration',
            name='ticket_type',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]