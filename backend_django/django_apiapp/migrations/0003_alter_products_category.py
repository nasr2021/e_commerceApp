# Generated by Django 4.2.4 on 2023-08-14 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_apiapp', '0002_category_order_remove_products_free_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(default='corps', on_delete=django.db.models.deletion.CASCADE, to='django_apiapp.category'),
        ),
    ]
