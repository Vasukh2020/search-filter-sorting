# Generated by Django 4.0.3 on 2022-06-15 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_alter_product_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='review',
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1),
        ),
    ]
