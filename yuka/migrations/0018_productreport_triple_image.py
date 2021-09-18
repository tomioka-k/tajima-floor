# Generated by Django 3.2.7 on 2021-09-18 06:10

from django.db import migrations, models
import yuka.function


class Migration(migrations.Migration):

    dependencies = [
        ('yuka', '0017_rename_rbg1_b_productreport_rgb1_b'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreport',
            name='triple_image',
            field=models.ImageField(blank=True, null=True, upload_to=yuka.function.upload_product_triple_image_path),
        ),
    ]
