# Generated by Django 4.2.7 on 2023-12-21 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_rename_placed_at_order_created_at_order_total_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitem_set', to='store.order'),
        ),
    ]
