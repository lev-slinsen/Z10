from django.contrib import admin
from .models import Pizza, Order, CreatePizza, Choice


class PizzaAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'size', 'weight', 'price', 'description', 'active')
    readonly_fields = ('id', )
    list_display = ('name', 'size', 'price', 'active')


admin.site.register(Pizza, PizzaAdmin)


# class OrderAdmin(admin.ModelAdmin):
#     fields = ('name', 'date', 'address', 'quantity', 'choice')
#     readonly_fields = ('id', )
#     list_display = ('name', 'date', 'quantity')
#
#
# admin.site.register(Order, OrderAdmin)


class CreatePizzaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )
    list_display = ('title', 'author', 'checked')


admin.site.register(CreatePizza, CreatePizzaAdmin)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['date']}),
        ('Address information', {'fields': ['address']})
    ]

    inlines = [ChoiceInline]
    list_display = ('name', 'address', 'date')

admin.site.register(Order, QuestionAdmin)
