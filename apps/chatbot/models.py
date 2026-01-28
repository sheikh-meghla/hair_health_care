from django.db import models

class HairImage(models.Model):
    image = models.ImageField(upload_to='hair_images/')
    created_at = models.DateTimeField(auto_now_add=True)
