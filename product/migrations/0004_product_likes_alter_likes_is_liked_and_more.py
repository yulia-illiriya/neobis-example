# Generated by Django 4.2.2 on 2023-07-03 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_price_currency_alter_product_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(default=None, related_name='liked_products', through='product.Likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='likes',
            name='is_liked',
            field=models.BooleanField(default=True, verbose_name='Понравилось'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='product.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Запись обновлена'),
        ),
    ]
