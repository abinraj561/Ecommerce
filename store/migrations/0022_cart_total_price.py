# Generated by Django 4.2.7 on 2023-12-21 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_rename_individual_price_orderitem_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
