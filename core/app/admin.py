from django.contrib import admin
from .models import House, Category, PaymentMethod



class HouseAdmin(admin.ModelAdmin):
    list_display = ('address', 'region', 'is_active')
    prepopulated_fields = {'slug': ('address', )}

admin.site.register(Category)
admin.site.register(House, HouseAdmin)
admin.site.register(PaymentMethod)
