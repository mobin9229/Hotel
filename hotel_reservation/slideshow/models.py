from django.db import models

class SlideshowImage(models.Model):
    image = models.ImageField(upload_to='slideshow/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)  # فرض کنید که این فیلد وجود دارد

    def __str__(self):
        return self.description or 'No Description'
