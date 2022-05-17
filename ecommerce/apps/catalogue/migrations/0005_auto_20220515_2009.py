# Generated by Django 3.2 on 2022-05-16 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20220515_1957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='productspecification',
            options={'verbose_name': 'Product Specification', 'verbose_name_plural': 'Product Specifications'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name': 'Product Type', 'verbose_name_plural': 'Product Types'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Required and unique', max_length=255, unique=True, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Category safe URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='Not Required', verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0 and 999.99.'}}, help_text='Maximum 999.99', max_digits=5, verbose_name='Discount price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Change product visibility', verbose_name='Product visibility'),
        ),
        migrations.AlterField(
            model_name='product',
            name='regular_price',
            field=models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0 and 999.99.'}}, help_text='Maximum 999.99', max_digits=5, verbose_name='Regular price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(help_text='Required', max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='productspecification',
            name='name',
            field=models.CharField(help_text='Required', max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='name',
            field=models.CharField(help_text='Required', max_length=255, unique=True, verbose_name='Product Name'),
        ),
    ]
