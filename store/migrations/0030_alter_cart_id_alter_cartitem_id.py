# Generated by Django 4.2.7 on 2023-12-21 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_remove_cartitem_individual_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]