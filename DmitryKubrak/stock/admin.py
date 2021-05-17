from django.contrib import admin
from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'size', 'weight', 'price', 'description', 'active')
    readonly_fields = ('id', )
    list_display = ('name', 'size', 'price', 'active')


admin.site.register(Pizza, PizzaAdmin)
