from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
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

class User(AbstractUser):
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='shop_user_groups',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='shop_user_permissions',
        related_query_name='user',
    )