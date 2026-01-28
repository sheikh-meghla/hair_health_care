from rest_framework import  serializers
from apps.landing_page.models import Features, FooterSection, HeroSection, HowItWorks, TakeTheGuessworkOutOfHairCare, TrustAndTransparency, WhyHairiSafeExists

class HeroSectionAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = ['id', 'title', 'subtitle', 'background_image']

class HowItWorksAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowItWorks
        fields = ['id', 'title', 'subtitle', 'image']

class WhyHairiSafeExistsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyHairiSafeExists
        fields = ['id', 'title', 'subtitle', 'image']

class FeaturesAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ['id', 'title', 'icon']

class TrustAndTransparencyAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustAndTransparency
        fields = ['id', 'title', 'icon']

class TakeTheGuessworkOutOfHairCareAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakeTheGuessworkOutOfHairCare
        fields = ['id', 'title', 'link']

class FooterSectionAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSection
        fields = ['id', 'title', 'icon', 'link']