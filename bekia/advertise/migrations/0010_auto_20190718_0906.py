# Generated by Django 2.1.5 on 2019-07-18 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0009_auto_20190715_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertise',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publisher', to=settings.AUTH_USER_MODEL),
        ),
    ]
