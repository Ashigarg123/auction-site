# Generated by Django 3.0.8 on 2020-07-20 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200720_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylist',
            name='bid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
