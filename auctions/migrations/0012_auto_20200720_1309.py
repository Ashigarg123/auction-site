# Generated by Django 3.0.8 on 2020-07-20 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20200720_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycomment',
            name='commented_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
