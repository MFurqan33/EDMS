from django.contrib import admin
from edmsapp.models import Contact,Order,Price,stockAvailable

# Register your models here.

#contact admin view
class ContAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message','date')
    search_fields=('name','email','subject','message','date')
    
    #list_editable=(' ',)

class OrderAdmin(admin.ModelAdmin):
    list_display=('order_id','invoice_number','user','quantity','payment','paid','address','delivery_status','date')
    search_fields=('user__username','invoice_number','payment','delivery_status')
    
    
class PriceAdmin(admin.ModelAdmin):
    list_display=('id','price',)
    list_editable=('price',)

class StockAdmin(admin.ModelAdmin):
    list_display=('id','Stock',)    

admin.site.register(Contact,ContAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Price,PriceAdmin)
admin.site.register(stockAvailable,StockAdmin)

