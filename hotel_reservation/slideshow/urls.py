from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SlideshowImageViewSet

router = DefaultRouter()
router.register(r'slideshow-images', SlideshowImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

