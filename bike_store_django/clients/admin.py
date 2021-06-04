from django.contrib import admin
from .models import Client, Order, Product, Choice

# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    fields = ('name',)
    readonly_fields = ('id',)
    list_display = ('name', )


admin.site.register(Client, ClientAdmin)


class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'size', 'description', 'brand', 'price', 'active')
    readonly_fields = ('id', )
    list_display = ('name', 'size', 'description', 'brand', 'price', 'active' )


admin.site.register(Product, ProductAdmin)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['date']}),
    ]

    inlines = [ChoiceInline]
    list_display = ('name', 'date', 'price', 'final_price')
    # list_display = ('name', 'date', 'final_price')


admin.site.register(Order, QuestionAdmin)
