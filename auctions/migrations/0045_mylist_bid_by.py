# Generated by Django 3.0.8 on 2020-07-24 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0044_remove_mylist_bid_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylist',
            name='bid_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mylist2', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
