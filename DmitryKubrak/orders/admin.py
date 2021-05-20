from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    fields = ('name', 'date', 'adress')
    readonly_fields = ('id', )
    list_display = ('name', 'date')


admin.site.register(Order, OrderAdmin)
