from django.contrib import admin
from .models import Pizza
# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
    pass





admin.site.register(Pizza,PizzaAdmin)