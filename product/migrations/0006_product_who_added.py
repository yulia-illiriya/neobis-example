# Generated by Django 4.2.2 on 2023-07-04 03:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0005_alter_price_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='who_added',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users_product', to=settings.AUTH_USER_MODEL, verbose_name='Кем добавлен'),
        ),
    ]