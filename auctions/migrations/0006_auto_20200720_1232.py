# Generated by Django 3.0.8 on 2020-07-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200720_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybid',
            name='bid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='mylist',
            name='bid',
            field=models.IntegerField(null=True),
        ),
    ]