from rest_framework import serializers
from .models import *


class PriceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Price
        fields = ['id', 'amount']
        
        
class PhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Photo
        fields = "__all__"
        

class ProductSerializer(serializers.ModelSerializer):
    price = PriceSerializer()
    photo = PhotoSerializer()   
    
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
            ]