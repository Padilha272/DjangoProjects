from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} ({self.id})"

class Product(models.Model):
    name = models.CharField(max_length=38)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    volume = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=48)

    def __str__(self):
        return f"{self.name} ({self.id})" 

User = get_user_model()

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)    