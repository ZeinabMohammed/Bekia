# Generated by Django 2.1.5 on 2019-06-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0005_advertise_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='contact',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]