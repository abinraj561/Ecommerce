# Generated by Django 4.2.7 on 2023-12-21 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_cartitem_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='individual_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='total_amount',
            new_name='total_price',
        ),
    ]
