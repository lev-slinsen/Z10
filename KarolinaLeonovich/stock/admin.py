from django.contrib import admin
from .models import Pizza, Ingredient, Order, ShopingCar


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    fields = ("active", "name", "engname", "weight", "price", "description", "ingredients", "comment", "creator")

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(ShopingCar)
class ShopingCarAdmin(admin.ModelAdmin):
    pass