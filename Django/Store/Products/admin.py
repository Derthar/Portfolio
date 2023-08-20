from django.contrib import admin
from Products.models import ProductCategory, Product, Basket

# Register your models here.

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ('name', 'category', 'description', ('price', 'quantity'), 'image')
    search_fields = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
