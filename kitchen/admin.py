from django.contrib import admin
from.models import kitchenstaff

# Register your models here.
class kitchenstaffAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(kitchenstaff, kitchenstaffAdmin)