from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from shop.models import Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)

User = get_user_model()  # Obtenha o modelo de usuário personalizado
admin.site.register(User, UserAdmin)  # Não é necessário desregistrar o usuário

