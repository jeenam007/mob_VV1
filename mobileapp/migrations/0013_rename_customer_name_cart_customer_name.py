# Generated by Django 5.1.1 on 2025-04-14 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobileapp', '0012_cart_customer_name_cart_email_id_cart_mob_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Customer_name',
            new_name='customer_name',
        ),
    ]
