# Generated by Django 3.2.7 on 2021-09-16 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yuka', '0007_auto_20210916_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='yuka.series', verbose_name='シリーズ'),
        ),
    ]