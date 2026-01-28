from django.db import models

# Create your models here.
class FooterSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)

    def __str__(self):
        return self.title
class HowItWorks(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)

    def __str__(self):
        return self.title