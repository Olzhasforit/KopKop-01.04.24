from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer, AdditionalImageSerializer
from .models import Laptop
from .serializers import LaptopSerializer
from .models import PlayStation
from .serializers import PlayStationSerializer
from .models import SmallProduct
from .serializers import SmallProductSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LaptopListCreate(generics.ListCreateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

class LaptopRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


class PlayStationListCreate(generics.ListCreateAPIView):
    queryset = PlayStation.objects.all()
    serializer_class = PlayStationSerializer

class PlayStationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayStation.objects.all()
    serializer_class = PlayStationSerializer


class SmallProductListCreate(generics.ListCreateAPIView):
    queryset = SmallProduct.objects.all()
    serializer_class = SmallProductSerializer

class SmallProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SmallProduct.objects.all()
    serializer_class = SmallProductSerializer