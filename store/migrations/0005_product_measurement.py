# Generated by Django 5.0.3 on 2024-03-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='measurement',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
