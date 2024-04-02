from django.contrib import admin
from .models import Product, AdditionalImage, Laptop, AdditionalImageLaptop
from .models import PlayStation, AdditionalImagePlayStation, SmallProduct, AdditionalImageSmallProduct


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage

class AdditionalImageLaptopInline(admin.TabularInline):
    model = AdditionalImageLaptop

class AdditionalImagePlayStationInline(admin.TabularInline):
    model = AdditionalImagePlayStation

class AdditionalImageSmallProductInline(admin.TabularInline):
    model = AdditionalImageSmallProduct



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [AdditionalImageInline]  # Ваши существующие настройки

    # Определение действия "Copy products"
    actions = ['copy_products']

    def copy_products(self, request, queryset):
        for product in queryset:
            # Создание копии продукта с очисткой первичного ключа
            product.pk = None
            product.save()

        # Вывод сообщения об успешном копировании
        self.message_user(request, "Selected products have been copied successfully.")

    copy_products.short_description = "Copy selected products"


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    inlines = [AdditionalImageLaptopInline]

@admin.register(PlayStation)
class PlayStationAdmin(admin.ModelAdmin):
    inlines = [AdditionalImagePlayStationInline]

@admin.register(SmallProduct)
class SmallProductAdmin(admin.ModelAdmin):
    inlines = [AdditionalImageSmallProductInline]

@admin.register(AdditionalImage)
class AdditionalImageAdmin(admin.ModelAdmin):
    pass

@admin.register(AdditionalImageLaptop)
class AdditionalImageLaptopAdmin(admin.ModelAdmin):
    pass

@admin.register(AdditionalImagePlayStation)
class AdditionalImagePlayStationAdmin(admin.ModelAdmin):
    pass


