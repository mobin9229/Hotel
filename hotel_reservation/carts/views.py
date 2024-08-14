# carts/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        # محدود کردن نمایش Cart فقط برای کاربر جاری
        user = self.request.user
        if user.is_authenticated:
            return Cart.objects.filter(user=user)
        return Cart.objects.none()
    
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
