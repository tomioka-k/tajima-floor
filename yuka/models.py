import matplotlib.pyplot as plt
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.safestring import mark_safe
from .function import upload_product_image_path, upload_product_triple_image_path
from .views_modules.hsv_report import get_hsv_report, plt2png
from .views_modules.rgb_report import ImageReport
import matplotlib
from django.core.files.uploadedfile import InMemoryUploadedFile
import io
from config.settings import BASE_DIR
matplotlib.use('Agg')


class Series(models.Model):
    code = models.CharField(verbose_name="シリーズCD",
                            primary_key=True, max_length=255)
    name = models.CharField(verbose_name="シリーズ名", max_length=50)
    kana_name = models.CharField(verbose_name="シリーズ名(かな)", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "シリーズ"
        verbose_name_plural = "シリーズ"


class Variety(models.Model):
    code = models.CharField(verbose_name="品種CD",
                            primary_key=True, max_length=255)
    name = models.CharField(verbose_name="品種名", max_length=50)
    kana_name = models.CharField(verbose_name="品種名(かな)", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "品種"
        verbose_name_plural = "品種"


class Product(models.Model):
    unit_choices = (
        ("m", "m"),
        ("㎡", "㎡"),
        ("ケース", "ケース"),
        ("セット", "セット"),
        ("巻", "巻"),
        ("箱", "箱"),
        ("本", "本"),
        ("枚", "枚"),
    )

    code = models.CharField(verbose_name="品名CD",
                            primary_key=True, max_length=255)
    series = models.ForeignKey(
        Series, verbose_name="シリーズ", on_delete=models.CASCADE, blank=True, null=True)
    variety = models.ForeignKey(
        Variety, verbose_name="品種", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(verbose_name="品名", max_length=50)
    sales_unit = models.CharField(
        verbose_name="販売単位", choices=unit_choices, max_length=20, blank=True, null=True)
    catalog_retail_price = models.IntegerField(
        verbose_name="カタログ上代価格", validators=[MinValueValidator(0), ], blank=True, null=True)
    catalog_retail_unit = models.CharField(
        verbose_name="カタログ上代単位", choices=unit_choices, max_length=20, blank=True, null=True)
    thickness = models.FloatField(verbose_name="厚み(mm)", blank=True, null=True)
    standard = models.CharField(
        verbose_name="規格", max_length=100, blank=True, null=True)
    display_standard = models.CharField(
        verbose_name="表示用規格", max_length=100, blank=True, null=True)
    retail_price = models.IntegerField(
        verbose_name="上代", validators=[MinValueValidator(0), ], blank=True, null=True)
    expenses = models.IntegerField(
        verbose_name="入目", validators=[MinValueValidator(0), ], blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.name, self.code)

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"


class ProductReport(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_product_image_path)
    triple_image = models.ImageField(
        upload_to=upload_product_triple_image_path, blank=True, null=True)
    hsv_report = models.BinaryField(blank=True, null=True)

    h_per_5 = models.FloatField(blank=True, null=True)
    h_per_50 = models.FloatField(blank=True, null=True)
    h_per_95 = models.FloatField(blank=True, null=True)
    s_per_5 = models.FloatField(blank=True, null=True)
    s_per_50 = models.FloatField(blank=True, null=True)
    s_per_95 = models.FloatField(blank=True, null=True)
    v_per_5 = models.FloatField(blank=True, null=True)
    v_per_50 = models.FloatField(blank=True, null=True)
    v_per_95 = models.FloatField(blank=True, null=True)

    rgb1_r = models.FloatField(blank=True, null=True)
    rgb1_g = models.FloatField(blank=True, null=True)
    rgb1_b = models.FloatField(blank=True, null=True)
    rgb2_r = models.FloatField(blank=True, null=True)
    rgb2_g = models.FloatField(blank=True, null=True)
    rgb2_b = models.FloatField(blank=True, null=True)
    rgb3_r = models.FloatField(blank=True, null=True)
    rgb3_g = models.FloatField(blank=True, null=True)
    rgb3_b = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.product, self.image)

    def scheme_image_tag(self):
        if self.hsv_report != None:
            from base64 import b64encode
            return mark_safe('<img src = "data: image/png; base64, {}" height="300">'.format(
                b64encode(self.hsv_report).decode('utf8')
            ))

    scheme_image_tag.short_description = 'HSV_Report'
    scheme_image_tag.allow_tags = True

    def save(self, **kwargs):
        super(ProductReport, self).save(**kwargs)
        image_path = str(BASE_DIR)+str(self.image.url)
        imagereport = ImageReport(image_path)
        triple_image = imagereport.triple_color_image()
        image_io = io.BytesIO()
        triple_image.save(image_io, format="png")
        triple_image_file = InMemoryUploadedFile(image_io, field_name=None, name="triple_image",
                                                 content_type="image/png", size=image_io.getbuffer().nbytes,
                                                 charset=None)
        self.triple_image = triple_image_file
        hsv = get_hsv_report(image_path)
        report_binary = plt2png()
        self.hsv_report = report_binary
        self.h_per_5 = hsv['h_per_5']
        self.h_per_50 = hsv['h_per_50']
        self.h_per_95 = hsv['h_per_95']
        self.s_per_5 = hsv['s_per_5']
        self.s_per_50 = hsv['s_per_50']
        self.s_per_95 = hsv['s_per_95']
        self.v_per_5 = hsv['v_per_5']
        self.v_per_50 = hsv['v_per_50']
        self.v_per_95 = hsv['v_per_95']
        super(ProductReport, self).save(**kwargs)
