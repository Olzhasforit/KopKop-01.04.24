from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    name_template = models.TextField()
    description = models.TextField()
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', null=True)
    characteristics = models.TextField()
    display = models.TextField()
    cpu = models.TextField()
    camera = models.TextField()
    battery = models.TextField()
    size = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AdditionalImage(models.Model):
    product = models.ForeignKey(Product, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='additional_images/')

    def __str__(self):
        return f'Additional Image {self.id}'

class Laptop(models.Model):
    name = models.CharField(max_length=100)
    name_template = models.TextField(default='Unknown')
    description = models.TextField(default='')
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', null=True)
    characteristics = models.TextField(default='')
    display = models.TextField(default='Unknown')
    cpu = models.TextField(default='Unknown')
    camera = models.TextField(default='')
    battery = models.TextField(default='')
    size = models.TextField(default='Unknown')
    category = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class AdditionalImageLaptop(models.Model):
    laptop = models.ForeignKey(Laptop, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='additional_images/')

    def __str__(self):
        return f'Additional Image {self.id} for Laptop {self.laptop.name}'



class PlayStation(models.Model):
    name = models.CharField(max_length=100)
    name_template = models.TextField(default='Unknown')
    description = models.TextField(default='')
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', null=True)
    characteristics = models.TextField(default='')
    cpu = models.TextField(default='Unknown')
    display = models.TextField(default='Unknown')
    information = models.TextField(default='')
    size = models.TextField(default='Unknown')
    category = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class AdditionalImagePlayStation(models.Model):
    PlayStation = models.ForeignKey(PlayStation, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='additional_images/')

    def __str__(self):
        return f'Additional Image {self.id} for PlayStation {self.PlayStation.name}'


class SmallProduct(models.Model):
    name = models.CharField(max_length=100)
    name_template = models.TextField(default='Unknown')
    description = models.TextField(default='')
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', null=True)
    characteristics = models.TextField(default='')
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AdditionalImageSmallProduct(models.Model):
    SmallProduct = models.ForeignKey(SmallProduct, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='additional_images/')

    def __str__(self):
        return f'Additional Image {self.id} for SmallProduct {self.SmallProduct.name}'