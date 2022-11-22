# Generated by Django 4.0.6 on 2022-11-16 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_detail_products_product_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_detail',
        ),
        migrations.AddField(
            model_name='products',
            name='product_detail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.detail'),
            preserve_default=False,
        ),
    ]
