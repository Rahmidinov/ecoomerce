# Generated by Django 4.1.7 on 2023-04-06 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitems',
            old_name='products',
            new_name='product',
        ),
    ]