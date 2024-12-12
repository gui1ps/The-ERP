# Generated by Django 5.1.3 on 2024-12-10 00:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_unit'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='products.products'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
