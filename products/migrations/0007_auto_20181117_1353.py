# Generated by Django 2.1.2 on 2018-11-17 13:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20181112_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_documents',
        ),
        migrations.AddField(
            model_name='product',
            name='product_document',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='product_document'),
            preserve_default=False,
        ),
    ]