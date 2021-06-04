from django.contrib import admin
from django.db.models import F

from .models import Stock
from .models import Order


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    fields = ('name', 'price')
    list_display = ('name', 'price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('id', 'parts', 'date', 'qty', 'price')
    readonly_fields = ('id', 'price',)
    list_display = ('date', 'qty', 'price')
