from django.contrib import admin
from .models import Pizza
from .models import Order


class PizzaAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'weight', 'price', 'description', 'isActive')
    readonly_fields = ('id',)
    list_display = ('name', 'price', 'isActive')


admin.site.register(Pizza, PizzaAdmin)


class OrderAdmin(admin.ModelAdmin):
    fields = ('your_name', 'date_time', 'address', 'pizza')
    list_display = ('your_name', 'date_time', 'address', 'pizza')


admin.site.register(Order, OrderAdmin)
