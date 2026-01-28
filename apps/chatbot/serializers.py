from rest_framework import serializers
from .models import HairImage

class HairImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HairImage
        fields = ['id', 'image']