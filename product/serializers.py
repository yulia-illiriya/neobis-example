from rest_framework import serializers
from .models import *


class PriceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Price
        fields = ['amount', "currency"]
        
        
class PhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Photo
        fields = "__all__"
        
        
class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Likes
        fields = ('is_liked',)
        

class ProductSerializer(serializers.ModelSerializer):
    price = PriceSerializer()
    photo = PhotoSerializer(many=True)
    amount_of_likes = serializers.ReadOnlyField()
    
    def create(self, validated_data):
        price_data = validated_data.pop('price', None)
        photo_data = validated_data.pop('photo', None)
        likes_data = validated_data.pop('likes', None)

        product = Product.objects.create(**validated_data)

        if price_data:
            price, _ = Price.objects.get_or_create(product=product, **price_data)
            product.price = price

        if photo_data:
            photo_instances = []
            for data in photo_data:
                photo_instance = Photo.objects.create(product=product, **data)
                photo_instances.append(photo_instance)
            product.photo = photo_instances[0]  # Присвоить первое фото как основное

        if likes_data:
            likes_instances = []
            for data in likes_data:
                user = data.get('user')
                like, _ = Likes.objects.get_or_create(product=product, user=user)
                like.is_liked = True
                like.save()
                likes_instances.append(like)
            product.likes.set(likes_instances)

        product.save()

        return product
    
    class Meta:
        model = Product
        fields = [
            'name_of_product', 
            'short_description', 
            'description',
            'amount_of_likes',
            'price',
            'photo',
            'created_at',  
            'updated_at', 
            ]