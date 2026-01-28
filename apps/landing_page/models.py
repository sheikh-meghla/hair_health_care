from django.db import models


class HeroSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    background_image = models.ImageField(upload_to='hero_section/')

    def __str__(self):
        return self.title
    
class HowItWorks(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='how_it_works/')

    def __str__(self):
        return self.title
    
class WhyHairiSafeExists(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='why_hairisafe_exists/')

    def __str__(self):
        return self.title
    
class Features(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='features_icons/')
    
    def __str__(self):
        return self.title
    
class TrustAndTransparency(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='trust_and_transparency_icons/')

    def __str__(self):
        return self.title
    
class TakeTheGuessworkOutOfHairCare(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    
    def __str__(self):
        return self.title

class FooterSection(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='footer_section_icons/')
    link = models.URLField()    
    def __str__(self):
        return self.title