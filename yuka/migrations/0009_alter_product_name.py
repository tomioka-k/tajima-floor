# Generated by Django 3.2.7 on 2021-09-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuka', '0008_alter_product_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='品名'),
        ),
    ]