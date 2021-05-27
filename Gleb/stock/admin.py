from django.contrib import admin
from .models import Pizza, Ingredient


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'weight', 'price', 'description', 'ingredients', 'size')
    readonly_fields = ('id',)
    list_display = ('name', 'price')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
