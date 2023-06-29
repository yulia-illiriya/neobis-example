from django.db import models

class Price(models.Model):
    amount = models.DecimalField("Стоимость", max_digits=9, decimal_places=2)
    is_active = models.BooleanField("Актуальна ли?", default=True)
    
    def __str__(self) -> str:
        return f"{self.amount}"
    
    class Meta:
        verbose_name = "Цена"
        verbose_name = "Цены"
        
class Photo(models.Model):
    photo_url = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    uploaded_at = models.DateTimeField("Фото загружено", auto_now_add=True)
    title = models.CharField("Описание", default="Sample")
    
    def __str__(self):
        return self.title

class Product(models.Model):
    name_of_product = models.CharField("Product", max_length=100)
    short_description = models.CharField("Shorts", max_length=250)
    description = models.TextField("Full description")
    created_at = models.DateTimeField("Запись создана", auto_now_add=True)
    updated_at = models.DateTimeField("Запись обновлена", auto_now_add=True)
    price = models.ForeignKey(Price, related_name="product", on_delete=models.SET_NULL, null=True)
    amount_of_likes = models.PositiveBigIntegerField("Нравится", default=0)
    
    def __str__(self):
        return self.name_of_product
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Basket(models.Model):
    product = models.ForeignKey(Product, related_name="basket", on_delete=models.CASCADE)
    created_at = models.DateTimeField("Корзина создана", auto_now_add=True)
    is_completed = models.BooleanField("Корзина собрана?", default=False)
    