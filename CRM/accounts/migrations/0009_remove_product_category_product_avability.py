# Generated by Django 4.0.2 on 2022-03-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_order_tags_product_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='avability',
            field=models.CharField(choices=[('stock', 'stock'), ('Out of stock', 'Out of stock')], max_length=200, null=True),
        ),
    ]
