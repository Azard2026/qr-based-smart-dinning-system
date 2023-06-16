from django.contrib import admin
from .models import orders,customercall ,tablenumber
# Register your models here.
class ordersAdmin(admin.ModelAdmin):
    list_display = ('orderid', 'tablenumber','itemname','itemquantity','itemprice','date','orderstatus')

admin.site.register(orders, ordersAdmin)
class customercallAdmin(admin.ModelAdmin):
    list_display = ('tablecall',)

admin.site.register(customercall, customercallAdmin)

class tablenumberAdmin(admin.ModelAdmin):
    list_display = ('tablename',)

admin.site.register(tablenumber, tablenumberAdmin)
