# Generated by Django 3.2.7 on 2021-09-18 01:34

from django.db import migrations, models
import django.db.models.deletion
import yuka.function


class Migration(migrations.Migration):

    dependencies = [
        ('yuka', '0015_auto_20210917_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(
                    upload_to=yuka.function.upload_product_image_path)),
                ('hsv_report', models.BinaryField(blank=True, null=True)),
                ('h_per_5', models.FloatField(blank=True, null=True)),
                ('h_per_50', models.FloatField(blank=True, null=True)),
                ('h_per_95', models.FloatField(blank=True, null=True)),
                ('s_per_5', models.FloatField(blank=True, null=True)),
                ('s_per_50', models.FloatField(blank=True, null=True)),
                ('s_per_95', models.FloatField(blank=True, null=True)),
                ('v_per_5', models.FloatField(blank=True, null=True)),
                ('v_per_50', models.FloatField(blank=True, null=True)),
                ('v_per_95', models.FloatField(blank=True, null=True)),
                ('rgb1_r', models.FloatField(blank=True, null=True)),
                ('rgb1_g', models.FloatField(blank=True, null=True)),
                ('rbg1_b', models.FloatField(blank=True, null=True)),
                ('rgb2_r', models.FloatField(blank=True, null=True)),
                ('rgb2_g', models.FloatField(blank=True, null=True)),
                ('rgb2_b', models.FloatField(blank=True, null=True)),
                ('rgb3_r', models.FloatField(blank=True, null=True)),
                ('rgb3_g', models.FloatField(blank=True, null=True)),
                ('rgb3_b', models.FloatField(blank=True, null=True)),
                ('product', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='yuka.product')),
            ],
        ),
        migrations.DeleteModel(
            name='HSVReport',
        ),
        migrations.DeleteModel(
            name='ProductRGB',
        ),
    ]
