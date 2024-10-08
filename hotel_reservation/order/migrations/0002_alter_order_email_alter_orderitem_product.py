# Generated by Django 5.0.7 on 2024-08-12 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
        ("product", "0003_product_number_of_beds"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="email",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="product.product",
            ),
        ),
    ]
