from django.contrib import admin
from .models import drink,sandwich,pizza ,hotdrink, milkshack,chaat,ourspecial

# Register your models here.
class pizzasAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(pizza, pizzasAdmin)



class drinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(drink, drinksAdmin)

class sandwichAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(sandwich, sandwichAdmin)

class hotdrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(hotdrink, hotdrinkAdmin)

class chaatAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(chaat, chaatAdmin)

class ourspecialAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(ourspecial, ourspecialAdmin)


class milkshackAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(milkshack, milkshackAdmin)

# class ordersAdmin(admin.ModelAdmin):
#     list_display = ('item', 'total','date')

# admin.site.register(orders, ordersAdmin)

# class tablenumberAdmin(admin.ModelAdmin):
#     list_display = ('tablename',)

# admin.site.register(tablenumber, tablenumberAdmin)