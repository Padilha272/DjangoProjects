from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 30)

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
