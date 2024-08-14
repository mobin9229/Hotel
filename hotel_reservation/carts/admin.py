# carts/admin.py
from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1  # تعداد فرم‌های اضافی برای افزودن آیتم‌های جدید

class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)  # نمایش نام کاربر در لیست
    inlines = [CartItemInline]  # افزودن فرم‌های CartItem به صفحه Cart

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')  # نمایش اطلاعات آیتم‌ها

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
