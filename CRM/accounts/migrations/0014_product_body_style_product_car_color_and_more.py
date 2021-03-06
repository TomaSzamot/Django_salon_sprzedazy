# Generated by Django 4.0.2 on 2022-04-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_rename_engine_capacity_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='body_style',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='car_color',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_model',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('reserved', 'reserved'), ('available', 'available'), ('sold', 'sold')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='avability',
            field=models.CharField(choices=[('in stock', 'in stock'), ('to order', 'to order')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
