
from django.contrib import admin
from .models import Product,ProductReview

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductReview)

# class BookStoreModelAdmin(admin.ModelAdmin):
#     list_display = ('id','book_name','author','category','first_pub','last_pub')

# admin.site.register(BookStoreModel, BookStoreModelAdmin)