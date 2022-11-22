# Generated by Django 4.0.6 on 2022-11-16 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_remove_products_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='is_discount',
        ),
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.brand'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_detail',
        ),
        migrations.AddField(
            model_name='products',
            name='product_detail',
            field=models.ManyToManyField(blank=True, to='blog.detail'),
        ),
    ]
