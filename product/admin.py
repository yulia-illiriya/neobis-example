from django.contrib import admin
from .models import Price, Product, Photo, Likes

admin.site.register(Product)
admin.site.register(Price)
admin.site.register(Photo)
admin.site.register(Likes)
