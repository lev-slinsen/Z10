from django.contrib import admin
from .models import Pizza, Order, CreatePizza


class PizzaAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'size', 'weight', 'price', 'description', 'active')
    readonly_fields = ('id', )
    list_display = ('name', 'size', 'price', 'active')


admin.site.register(Pizza, PizzaAdmin)


class OrderAdmin(admin.ModelAdmin):
    fields = ('name', 'date', 'address', 'quantity', 'choice')
    readonly_fields = ('id', )
    list_display = ('name', 'date', 'quantity')


admin.site.register(Order, OrderAdmin)


class CreatePizzaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )
    list_display = ('title', 'author', 'checked')

admin.site.register(CreatePizza, CreatePizzaAdmin)
