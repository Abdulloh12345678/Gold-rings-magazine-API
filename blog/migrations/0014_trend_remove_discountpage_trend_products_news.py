# Generated by Django 4.0.6 on 2022-11-15 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_products_trends_discountpage_trend_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='discountpage',
            name='trend',
        ),
        migrations.AddField(
            model_name='products',
            name='news',
            field=models.ManyToManyField(to='blog.trend'),
        ),
    ]