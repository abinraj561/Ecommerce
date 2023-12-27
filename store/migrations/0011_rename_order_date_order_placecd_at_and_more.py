# Generated by Django 4.2.7 on 2023-12-21 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0010_alter_orderitem_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_date',
            new_name='placecd_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='store.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.product'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
