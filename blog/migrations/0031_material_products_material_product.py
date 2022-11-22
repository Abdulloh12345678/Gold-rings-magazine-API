# Generated by Django 4.0.6 on 2022-11-16 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_remove_products_product_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='material_product',
            field=models.ManyToManyField(to='blog.material'),
        ),
    ]
