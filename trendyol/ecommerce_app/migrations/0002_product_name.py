# Generated by Django 5.0 on 2023-12-28 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='Ürün Adı', max_length=255),
        ),
    ]