# Generated by Django 4.2.7 on 2023-12-25 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_cartitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
    ]
