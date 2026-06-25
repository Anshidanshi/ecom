from django.contrib import admin
from .models import Category, Product, ProductColorImage, ProductVariant


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display        = ['name', 'slug', 'is_active', 'created_at']
    list_filter         = ['is_active']
    search_fields       = ['name']
    prepopulated_fields = {'slug': ('name',)}


class ProductColorImageInline(admin.TabularInline):
    model = ProductColorImage
    extra = 1


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display        = ['name', 'category', 'price', 'is_available', 'is_featured', 'created_at']
    list_filter         = ['category', 'is_available', 'is_featured']
    list_editable       = ['price', 'is_available']
    search_fields       = ['name']
    prepopulated_fields = {'slug': ('name',)}
    inlines             = [ProductColorImageInline, ProductVariantInline]


@admin.register(ProductColorImage)
class ProductColorImageAdmin(admin.ModelAdmin):
    list_display  = ['product', 'color', 'image']
    search_fields = ['product__name', 'color']


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display  = ['product', 'color', 'size', 'stock', 'sku']
    list_editable = ['stock']
    search_fields = ['sku', 'product__name']
    list_filter   = ['color', 'size']