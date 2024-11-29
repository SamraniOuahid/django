# Generated by Django 5.1.3 on 2024-11-27 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='products',
        ),
        migrations.AddField(
            model_name='user',
            name='products',
            field=models.ManyToManyField(null=True, to='pages.product'),
        ),
    ]