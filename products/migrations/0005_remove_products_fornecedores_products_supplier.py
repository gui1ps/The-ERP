# Generated by Django 5.1.3 on 2024-12-19 00:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_unit'),
        ('suppliers', '0002_alter_suppliers_postal_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='fornecedores',
        ),
        migrations.AddField(
            model_name='products',
            name='supplier',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='suppliers.suppliers'),
        ),
    ]