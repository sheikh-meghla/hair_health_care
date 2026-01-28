from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import (
    FooterSectionAdminSerializer,
    HeroSectionAdminSerializer,
    HowItWorksAdminSerializer,
    TakeTheGuessworkOutOfHairCareAdminSerializer,
    WhyHairiSafeExistsAdminSerializer,
    FeaturesAdminSerializer,
    TrustAndTransparencyAdminSerializer,
    TakeTheGuessworkOutOfHairCareAdminSerializer,
    FooterSectionAdminSerializer
)

class HeroSectionAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        hero_sections = HeroSectionAdminSerializer.objects.all()
        serializer = HeroSectionAdminSerializer(hero_sections, many=True)
        return Response({
            "status" : "success",
            "data" : serializer.data
        })
    
class HowItWorksAdminAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        how_it_works = HowItWorksAdminSerializer.objects.all()
        serializer = HowItWorksAdminSerializer(how_it_works, many=True)
        return Response({
            "status" : "success",
            "data" : serializer.data
        })
    
class WhyHairiSafeExistsAdminAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        why_hairisafe_exists = WhyHairiSafeExistsAdminSerializer.objects.all()
        serializer = WhyHairiSafeExistsAdminSerializer(why_hairisafe_exists, many=True)
        return Response({
            "status" : "success",
            "data" : serializer.data
        })
    
class FeaturesAdminAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        features = FeaturesAdminSerializer.objects.all()
        serializer = FeaturesAdminSerializer(features, many=True)
        return Response({
            "status" : "success",
            "data" : serializer.data
        })
    
class TrustAndTransparencyAdminAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        trust_and_transparency = TrustAndTransparencyAdminSerializer.objects.all()
        serializer = TrustAndTransparencyAdminSerializer(trust_and_transparency, many=True)
        return Response({
            "status" : "success",
            "data" : serializer.data
        })

class TakeTheGuessworkOutOfHairCareAdminAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        take_the_guesswork_out_of_hair_care = TakeTheGuessworkOutOfHairCareAdminSerializer.objects.all()
        serializer = TakeTheGuessworkOutOfHairCareAdminSerializer(take_the_guesswork_out_of_hair_care, many=True)
        return Response({
            "status" : "success",
            "data" : serializer.data
        })
    
class FooterSectionAdminAPIView(APIView):
    permission_classes = []
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        footer_sections = FooterSectionAdminSerializer.objects.all()
        serializer = FooterSectionAdminSerializer(footer_sections, many=True)
        return Response({
            "status" : "success",
            "data" : serializer.data
        })
    
