from django.contrib import admin
from .models import Pizza, Ingredient
from .models import Order


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'weight', 'price', 'description', 'ingredients', 'size')
    readonly_fields = ('id',)
    list_display = ('name', 'price')

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

class PurchaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, PurchaseAdmin)
