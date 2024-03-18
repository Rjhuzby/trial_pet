from django.contrib import admin

from .models import Product



admin.site.site_header = 'Администрирование сайта'
admin.site.site_title = 'Администрирование сайта'
admin.site.index_title = 'admin'



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)
    list_editable = ('price', 'description',)
    actions = ['make_zero']
    
    def make_zero(self, request, queryset):
        queryset.update(price=0)
    
admin.site.register(Product, ProductAdmin)
    