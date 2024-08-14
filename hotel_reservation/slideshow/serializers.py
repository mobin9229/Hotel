from rest_framework import serializers
from .models import SlideshowImage

class SlideshowImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideshowImage
        fields = ['image', 'description']
