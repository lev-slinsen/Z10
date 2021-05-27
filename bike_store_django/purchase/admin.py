from django.contrib import admin
from .models import Equipment


class EquipmentsAdmin(admin.ModelAdmin):
    fields = ('name', 'quantity', 'price', 'discount')


admin.site.register(Equipment, EquipmentsAdmin)
