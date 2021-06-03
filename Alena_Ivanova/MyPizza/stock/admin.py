from django.contrib import admin
from .models import Pizza, Order, PizzaDraft

class PizzaAdmin(admin.ModelAdmin):
    pass

class PizzaDarftAdmin(admin.ModelAdmin):
    pass

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(PizzaDraft, PizzaDarftAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Order, OrderAdmin)