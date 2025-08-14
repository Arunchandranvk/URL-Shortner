from django.db import models
from django.conf import settings
import os
from .utils import generate_short_code,generate_qr_code

class ShortURL(models.Model):
    name = models.CharField(max_length=100,null=True)
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            code = generate_short_code()
            while ShortURL.objects.filter(short_code=code).exists():
                code = generate_short_code()
            self.short_code = code
        if not self.qr_code:
            qr_image_path = generate_qr_code(f"{settings.BASE_URL}/{self.short_code}")
            self.qr_code.name = qr_image_path
        super().save(*args, **kwargs)

    def get_short_url(self):
        return f"{settings.BASE_URL}/{self.short_code}"

    def __str__(self):
        return self.short_code
