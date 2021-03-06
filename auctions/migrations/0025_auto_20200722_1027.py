# Generated by Django 3.0.8 on 2020-07-22 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='bid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='category',
            field=models.CharField(choices=[('Gadget', 'Gadget'), ('Phome', 'Phone'), ('Cloth', 'Cloth'), ('Furniture', 'Furniture'), ('vehicle', 'vehicle')], default='vehicle', max_length=20),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='current_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='msg',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='subject',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlist',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='url',
            field=models.URLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to=settings.AUTH_USER_MODEL),
        ),
    ]
