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
    photo = PhotoSerializer()
    likes = LikeSerializer()
    amount_of_likes = serializers.ReadOnlyField()
   
    
    class Meta:
        model = Product
        fields = [
            'name_of_product', 
            'short_description', 
            'description', 
            'created_at',  
            'updated_at', 
            'price',
            'amount_of_likes',
            'photo',
            'likes',
            ]