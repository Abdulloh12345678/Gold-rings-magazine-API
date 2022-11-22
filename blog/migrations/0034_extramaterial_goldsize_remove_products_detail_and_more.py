# Generated by Django 4.0.6 on 2022-11-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_products_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoldSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('count', models.IntegerField()),
                ('base_count', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='detail',
        ),
        migrations.AddField(
            model_name='detail',
            name='size',
            field=models.ManyToManyField(to='blog.goldsize'),
        ),
    ]