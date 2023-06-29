from django.contrib import admin
from .models import Price, Product, Photo

admin.site.register(Product)
admin.site.register(Price)
admin.site.register(Photo)
