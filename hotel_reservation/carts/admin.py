from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1  

class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)  
    inlines = [CartItemInline]  

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')  

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
