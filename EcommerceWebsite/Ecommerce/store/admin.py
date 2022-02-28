from django.contrib import admin
from .models import User, BuyerModel, SellerModel,OrderModel, ProductModel, CategoryModel

class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}


# Register your models here.
admin.site.register(User)
admin.site.register(BuyerModel)
admin.site.register(SellerModel)
admin.site.register(OrderModel)
admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(CategoryModel)