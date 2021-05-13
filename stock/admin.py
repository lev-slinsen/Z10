from django.contrib import admin
from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'size', 'weight', 'price', 'description', 'isActive')
    readonly_fields = ('id',)
    list_display = ('name', 'size', 'price', 'isActive')



admin.site.register(Pizza, PizzaAdmin)
