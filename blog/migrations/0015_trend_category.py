# Generated by Django 4.0.6 on 2022-11-15 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_trend_remove_discountpage_trend_products_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='trend',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
            preserve_default=False,
        ),
    ]
