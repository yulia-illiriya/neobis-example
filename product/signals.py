from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Likes, Product

@receiver(post_save, sender=Likes)
def update_product_likes(sender, instance, **kwargs):
    product = instance.product
    product.amount_of_likes = Likes.objects.filter(product=product).count()
    product.save()
    
@receiver(post_delete, sender=Likes)
def update_product_likes_on_delete(sender, instance, **kwargs):
    product = instance.product
    product.amount_of_likes = Likes.objects.filter(product=product).count()
    product.save()