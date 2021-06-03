from django.contrib import admin
from django.db.models import F

from .models import Stock
from .models import Order


class StockAdmin(admin.ModelAdmin):
    fields = ('name', 'price')
    list_display = ('name', 'price')


admin.site.register(Stock, StockAdmin)


class OrderAdmin(admin.ModelAdmin):
    fields = ('part', 'date', 'qty')
    list_display = ('part', 'date', 'qty', 'price')


    #def calculate(self, self, request, obj, form, change):
        #Order.objects.annotate(total_price=F('part') * F('qty'))


admin.site.register(Order, OrderAdmin)