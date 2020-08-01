# Generated by Django 3.0.8 on 2020-07-24 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0042_auto_20200724_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycomment',
            name='commented_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
