# Generated by Django 4.0.6 on 2022-11-16 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_extramaterial_goldsize_remove_products_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='detail',
            field=models.ManyToManyField(to='blog.detail'),
        ),
    ]
