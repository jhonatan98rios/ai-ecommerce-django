from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    fields = ('name', 'price', 'category', 'short_description', 'long_description', 'image')
    
admin.site.register(Product, ProductAdmin)