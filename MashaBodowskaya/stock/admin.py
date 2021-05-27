from django.contrib import admin
from .models import Pizza, CustomPizza
from .models import Order


class PizzaAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'weight', 'price', 'description', 'isActive')
    readonly_fields = ('id',)
    list_display = ('name', 'price', 'isActive')


admin.site.register(Pizza, PizzaAdmin)


class OrderAdmin(admin.ModelAdmin):
    fields = ('your_name', 'date_time', 'address', 'pizza')
    list_display = ('your_name', 'date_time', 'address', 'pizza')


admin.site.register(Order, OrderAdmin)


class CustomPizzaAdmin(admin.ModelAdmin):
    fields = ('auth_name', 'name', 'description', 'weight', 'isConfirmed')
    list_display = ('auth_name', 'name', 'description', 'weight', 'isConfirmed')



    # def save_model(self, request, obj, form, change):
    #     if obj.isConfirmed:
    #         a = CustomPizza():
    #         a.name = obj.save
    #     # d = CustomPizza.objects.filter(pk=1).values().first()
    #     # d.update({'isConfirmed': True})
    #     # duplicate = Pizza.objects.create(**d)
    #     super().save_model(request, obj, form, change)
    #
    #     #isconfirmed=True
    #     #create new Pizza in Pizza object
    #     #delete item from Custompizza object


admin.site.register(CustomPizza, CustomPizzaAdmin)
