# Generated by Django 5.1.3 on 2024-11-13 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='fornecedores',
            field=models.ManyToManyField(related_name='produtos', to='suppliers.suppliers'),
        ),
    ]
