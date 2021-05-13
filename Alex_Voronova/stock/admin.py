from django.contrib import admin
from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    #fields = ('id', 'name', 'size', 'weight', 'price', 'description')
    #readonly_fields = ('id',)
    #list_display = ('name', 'size', 'price')
    pass


admin.site.register(Pizza, PizzaAdmin)
