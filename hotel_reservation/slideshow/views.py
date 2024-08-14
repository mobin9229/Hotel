from rest_framework import viewsets
from .models import SlideshowImage
from .serializers import SlideshowImageSerializer

class SlideshowImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SlideshowImage.objects.all()
    serializer_class = SlideshowImageSerializer
