# Generated by Django 4.2.7 on 2023-12-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_rename_placecd_at_order_placed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
    ]
