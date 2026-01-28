# landing_page/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import (
    HeroSection,
    HowItWorks,
    WhyHairiSafeExists,
    Features,
    TrustAndTransparency,
    TakeTheGuessworkOutOfHairCare,
    FooterSection
)

from .serializers import (
    HeroSectionAdminSerializer,
    HowItWorksAdminSerializer,
    WhyHairiSafeExistsAdminSerializer,
    FeaturesAdminSerializer,
    TrustAndTransparencyAdminSerializer,
    TakeTheGuessworkOutOfHairCareAdminSerializer,
    FooterSectionAdminSerializer
)

# Hero Section API
class HeroSectionAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        hero_sections = HeroSection.objects.all()
        serializer = HeroSectionAdminSerializer(hero_sections, many=True)
        return Response({"status": "success", "data": serializer.data})


# How It Works API
class HowItWorksAdminAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        how_it_works = HowItWorks.objects.all()
        serializer = HowItWorksAdminSerializer(how_it_works, many=True)
        return Response({"status": "success", "data": serializer.data})


# Why HairiSafe Exists API
class WhyHairiSafeExistsAdminAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        why_hairisafe_exists = WhyHairiSafeExists.objects.all()
        serializer = WhyHairiSafeExistsAdminSerializer(why_hairisafe_exists, many=True)
        return Response({"status": "success", "data": serializer.data})


# Features API
class FeaturesAdminAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        features = Features.objects.all()
        serializer = FeaturesAdminSerializer(features, many=True)
        return Response({"status": "success", "data": serializer.data})


# Trust & Transparency API
class TrustAndTransparencyAdminAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        trust_and_transparency = TrustAndTransparency.objects.all()
        serializer = TrustAndTransparencyAdminSerializer(trust_and_transparency, many=True)
        return Response({"status": "success", "data": serializer.data})


# Take The Guesswork Out Of Hair Care API
class TakeTheGuessworkOutOfHairCareAdminAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        items = TakeTheGuessworkOutOfHairCare.objects.all()
        serializer = TakeTheGuessworkOutOfHairCareAdminSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data})


# Footer Section API
class FooterSectionAdminAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        footer_sections = FooterSection.objects.all()
        serializer = FooterSectionAdminSerializer(footer_sections, many=True)
        return Response({"status": "success", "data": serializer.data})
