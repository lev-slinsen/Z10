from django.contrib import admin
from .models import Client, Order, Product, Choice


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
        ('Id',               {'fields': ['id']}),
        ('Date information', {'fields': ['date']}),
        ('Price information', {'fields': ['price', 'price_after_discount']}),
        # ('One product information', {'fields': ['one_product_price']}),
    ]

    inlines = [ChoiceInline]
    list_display = ('name', 'date', 'price', 'price_after_discount')
    readonly_fields = ('id', 'price', 'price_after_discount')
    # readonly_fields = ('id', 'price', 'price_after_discount', 'one_product_price')


admin.site.register(Order, QuestionAdmin)
