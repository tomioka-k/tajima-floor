from django.contrib import admin
from django.db.models import fields
from .models import Series, Variety, Product, ProductReport
from django.utils.safestring import mark_safe

from import_export import resources
from import_export.admin import ExportMixin, ImportExportMixin


class SeriesResource(resources.ModelResource):
    class Meta:
        model = Series
        import_id_fields = ('code', )


class VarietyResource(resources.ModelResource):
    class Meta:
        model = Variety
        import_id_fields = ('code', )


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        import_id_fields = ('code', )
        fields = ('code', 'name', 'series', 'sales_unit')


class ProductReportResource(resources.ModelResource):
    class Meta:
        model = ProductReport
        fields = (
            'product__code', 'product__name',
            'rgb1_r', 'rgb1_g', 'rgb1_b',
            'rgb2_r', 'rgb2_g', 'rgb2_b',
            'rgb3_r', 'rgb3_g', 'rgb3_b',
            'h_per_5', 'h_per_50', 'h_per_95',
            's_per_5', 's_per_50', 's_per_95',
            'v_per_5', 'v_per_50', 'v_per_95'
        )
        export_order = (
            'product__code', 'product__name',
            'rgb1_r', 'rgb1_g', 'rgb1_b',
            'rgb2_r', 'rgb2_g', 'rgb2_b',
            'rgb3_r', 'rgb3_g', 'rgb3_b',
            'h_per_5', 'h_per_50', 'h_per_95',
            's_per_5', 's_per_50', 's_per_95',
            'v_per_5', 'v_per_50', 'v_per_95'
        )


@admin.register(Series)
class SeriesAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = SeriesResource
    list_display = ('name', 'kana_name', 'code')
    search_fields = ('name', 'kana_name')


@admin.register(Variety)
class VarietyAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = VarietyResource
    list_display = ('name', 'kana_name', 'code')
    search_fields = ('name', 'kana_name')


@admin.register(Product)
class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ProductResource
    search_fields = ('name',)
    list_display = ('name', 'series')
    list_filter = ('series', 'variety',)


@admin.register(ProductReport)
class ProductAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ProductReportResource
    search_fields = ('product', )
    list_display = (
        'product', 'display_image', "display_triple_image", 'scheme_image_tag'
    )
    readonly_fields = (
        'display_image', "display_triple_image", 'scheme_image_tag',
        'rgb1_r', 'rgb1_g', 'rgb1_b',
        'rgb2_r', 'rgb2_g', 'rgb2_b',
        'rgb3_r', 'rgb3_g', 'rgb3_b',
        'h_per_5', 'h_per_50', 'h_per_95',
        's_per_5', 's_per_50', 's_per_95',
        'v_per_5', 'v_per_50', 'v_per_95'
    )

    def display_image(self, obj):
        return mark_safe('<img src="{}" height="300;">'.format(obj.image.url))

    def display_triple_image(self, obj):
        if obj.triple_image:
            return mark_safe('<img src="{}" height="300;">'.format(obj.triple_image.url))
