"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from products.views import ProductListCreate, ProductRetrieveUpdateDestroy
from products.views import LaptopListCreate, LaptopRetrieveUpdateDestroy
from products.views import PlayStationListCreate, PlayStationRetrieveUpdateDestroy
from products.views import SmallProductListCreate, SmallProductRetrieveUpdateDestroy
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductListCreate.as_view(), name='product-list'),
    path('products/', ProductListCreate.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),
    path('api/laptops/', LaptopListCreate.as_view(), name='laptop-list'),
    path('api/laptops/<int:pk>/', LaptopRetrieveUpdateDestroy.as_view(), name='laptop-detail'),
    path('api/PlayStations/', PlayStationListCreate.as_view(), name='PlayStation-list'),
    path('api/PlayStations/<int:pk>/', PlayStationRetrieveUpdateDestroy.as_view(), name='PlayStation-detail'),
    path('api/SmallProducts/', SmallProductListCreate.as_view(), name='SmallProduct-list'),
    path('api/SmallProducts/<int:pk>/', SmallProductRetrieveUpdateDestroy.as_view(), name='SmallProduct-detail'),
]

# Добавляем URL-маршруты для обработки медиа-файлов в режиме разработки
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



