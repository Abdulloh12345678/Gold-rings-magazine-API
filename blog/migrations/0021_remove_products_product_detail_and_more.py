# Generated by Django 4.0.6 on 2022-11-16 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_remove_products_product_detail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_detail',
        ),
        migrations.AddField(
            model_name='discount',
            name='product_detail',
            field=models.ManyToManyField(to='blog.detail'),
        ),
    ]
