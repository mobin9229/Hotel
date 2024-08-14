from django.contrib import admin
from .models import SlideshowImage

class SlideshowImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'description', 'uploaded_at')  # مطمئن شوید که فیلدها به درستی نام‌گذاری شده‌اند
    search_fields = ('description',)  # یا هر فیلد دیگری که نیاز دارید

admin.site.register(SlideshowImage, SlideshowImageAdmin)
