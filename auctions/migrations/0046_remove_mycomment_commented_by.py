# Generated by Django 3.0.8 on 2020-07-24 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0045_mylist_bid_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycomment',
            name='commented_by',
        ),
    ]
