# Generated by Django 5.0.7 on 2024-08-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="number_of_beds",
            field=models.CharField(
                choices=[
                    ("single", "Single"),
                    ("double", "Double"),
                    ("triple", "Triple"),
                ],
                default="single",
                max_length=10,
            ),
        ),
    ]
