# Generated by Django 3.0.8 on 2020-07-25 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0047_auto_20200725_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='bid_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mylist2', to=settings.AUTH_USER_MODEL),
        ),
    ]
