# Generated by Django 3.2.7 on 2021-09-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuka', '0006_alter_product_variety'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catalog_retail_unit',
            field=models.CharField(blank=True, choices=[('m', 'm'), ('㎡', '㎡'), ('ケース', 'ケース'), ('セット', 'セット'), ('巻', '巻'), ('箱', '箱'), ('本', '本'), ('枚', '枚')], max_length=20, null=True, verbose_name='カタログ上代単位'),
        ),
        migrations.AlterField(
            model_name='product',
            name='display_standard',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='表示用規格'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sales_unit',
            field=models.CharField(blank=True, choices=[('m', 'm'), ('㎡', '㎡'), ('ケース', 'ケース'), ('セット', 'セット'), ('巻', '巻'), ('箱', '箱'), ('本', '本'), ('枚', '枚')], max_length=20, null=True, verbose_name='販売単位'),
        ),
        migrations.AlterField(
            model_name='product',
            name='standard',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='規格'),
        ),
    ]
