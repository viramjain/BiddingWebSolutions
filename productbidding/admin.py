from django.contrib import admin
from .models import Category,Productdetails,Orders,BidEntry,Bidwinner
from django.contrib.admin.options import ModelAdmin
class CategoryUserAdmin(ModelAdmin):

    list_display = ["title", "description"]
    search_fields = ["title", "description"]
    list_filter = ["title", "description"]
class ProductdetailsUserAdmin(ModelAdmin):
    list_display = ["ptitle", "price"]
    search_fields = ["ptitle", "price"]
    list_filter = ["ptitle", "price"]
class OrderUserAdmin(ModelAdmin):
    list_display = ["name", "order_id"]
    search_fields = ["name", "order_id"]
    list_filter = ["name", "order_id"]
class BidentryUserAdmin(ModelAdmin):
    list_display = ["fname", "useremail","product_id"]
    search_fields = ["fname", "useremail","product_id"]
    list_filter = ["fname", "useremail","product_id"]
class BidwinnersUserAdmin(ModelAdmin):
    list_display = ["fname", "useremail","product_id"]
    search_fields = ["fname", "useremail","product_id"]
    list_filter = ["fname", "useremail","product_id"]


admin.site.register(Category,CategoryUserAdmin)
admin.site.register(Productdetails,ProductdetailsUserAdmin)
admin.site.register(Orders,OrderUserAdmin)
admin.site.register(BidEntry,BidentryUserAdmin)
admin.site.register(Bidwinner,BidwinnersUserAdmin)
# Register your models here.
