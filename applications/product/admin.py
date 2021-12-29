from django.contrib import admin

from ..product.models import ProductImage, Product


class InlineProductImage(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', )


class ProductAdminDisplay(admin.ModelAdmin):
    inlines = [InlineProductImage, ]


admin.site.register(Product, ProductAdminDisplay)
