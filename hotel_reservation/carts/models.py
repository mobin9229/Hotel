# carts/models.py
from django.db import models
from django.conf import settings
from product.models import Product  # فرض می‌کنیم مدل Product در اپ product قرار دارد

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # دیگر فیلدها در صورت نیاز

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
