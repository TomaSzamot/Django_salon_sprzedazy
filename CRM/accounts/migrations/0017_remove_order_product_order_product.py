# Generated by Django 4.0.2 on 2022-04-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_product_car_color_alter_product_engine_fuel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(null=True, to='accounts.Product'),
        ),
    ]