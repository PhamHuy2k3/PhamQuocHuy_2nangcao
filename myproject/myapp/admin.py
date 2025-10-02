from django.contrib import admin
from .models import Post, Product, AboutDetail, Category

admin.site.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_best_selling', 'is_you_may_also_like')
    list_filter = ('category', 'is_best_selling', 'is_you_may_also_like')
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)
admin.site.register(AboutDetail)
admin.site.register(Category)
