# Generated by Django 4.0.6 on 2022-11-16 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_remove_products_is_discount_products_brand_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='brand',
        ),
        migrations.AlterField(
            model_name='products',
            name='product_detail',
            field=models.ManyToManyField(to='blog.detail'),
        ),
    ]
