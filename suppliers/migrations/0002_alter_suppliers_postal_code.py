# Generated by Django 5.1.3 on 2024-12-05 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliers',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]