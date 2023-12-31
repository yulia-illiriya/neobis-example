from django.db import models
from profile_user.models import User


class Price(models.Model):
    SOM = "KG"
    DOLLAR = "USD"
    EURO = "EU"
    RUBL = "RU"
    
    CURRENCY_CHOICES = [
        (SOM, "KG"),
        (DOLLAR, "USD"),
        (EURO,"EU"),
        (RUBL,"RU"),
        
    ]
    
    amount = models.DecimalField("Стоимость", max_digits=9, decimal_places=2)
    currency = models.CharField("Валюта", max_length=3, choices=CURRENCY_CHOICES, default=SOM)
    is_active = models.BooleanField("Актуальна ли?", default=True)
    
    def __str__(self) -> str:
        return f"{self.amount} {self.currency}"
    
    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
        
        
class Photo(models.Model):
    photo_url = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    title = models.CharField("Описание", default="Sample")
    
    def __str__(self):
        return self.title
    

class Likes(models.Model):
    is_liked = models.BooleanField("Понравилось", default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="like")
    
    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
        
    def unlike(self):
        self.delete()
    

class Product(models.Model):
    name_of_product = models.CharField("Product", max_length=100)
    short_description = models.CharField("Shorts", max_length=250)
    description = models.TextField("Full description")
    created_at = models.DateTimeField("Запись создана", auto_now_add=True)
    updated_at = models.DateTimeField("Запись обновлена", auto_now=True)
    price = models.ForeignKey(Price, related_name="product", on_delete=models.SET_NULL, null=True)
    amount_of_likes = models.PositiveBigIntegerField("Нравится", default=0)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, blank=True)
    likes = models.ManyToManyField(User, through='Likes', related_name="liked_products", default=None)
    who_added = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_product', verbose_name="Кем добавлен", default=1)
    
    def __str__(self):
        return self.name_of_product
    
    class Meta:
        ordering = ('name_of_product',)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"    
                

class Basket(models.Model):
    product = models.ForeignKey(Product, related_name="basket", on_delete=models.CASCADE)
    created_at = models.DateTimeField("Корзина создана", auto_now_add=True)
    is_completed = models.BooleanField("Корзина собрана?", default=False)
    user = models.ForeignKey(User, verbose_name="Пользователь", related_name="basket", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Корзина {self.user}"