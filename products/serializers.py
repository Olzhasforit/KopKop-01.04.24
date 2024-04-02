from rest_framework import serializers
from .models import Product, AdditionalImage, Laptop, PlayStation, SmallProduct


class AdditionalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalImage
        fields = ('id', 'image')

# Используйте стандартный ModelSerializer для модели Product
class ProductSerializer(serializers.ModelSerializer):
    additional_images = AdditionalImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class LaptopSerializer(serializers.ModelSerializer):
    additional_images = AdditionalImageSerializer(many=True, read_only=True)
    class Meta:
        model = Laptop
        fields = '__all__'

class PlayStationSerializer(serializers.ModelSerializer):
    additional_images = AdditionalImageSerializer(many=True, read_only=True)
    class Meta:
        model = PlayStation
        fields = '__all__'


class SmallProductSerializer(serializers.ModelSerializer):
    additional_images = AdditionalImageSerializer(many=True, read_only=True)
    class Meta:
        model = SmallProduct
        fields = '__all__'