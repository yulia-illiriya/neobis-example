from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Price, Photo, Product
from .serializers import ProductSerializer
from .models import Likes
from .permissions import IsVerifiedOrReadOnly
 
@swagger_auto_schema(tags=["Categories"])
class ProductListCreateView(generics.ListCreateAPIView):
    """Смотрим список всех товаров"""
    
    permission_classes = [IsVerifiedOrReadOnly,]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
@swagger_auto_schema(tags=["Categories"])
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """просто смотрим все товары детально"""
    
    permission_classes = [IsVerifiedOrReadOnly,]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class UserProductsView(generics.ListCreateAPIView):
    
    """просматриваем весь список товаров, добавленных этим юзером"""
    
    permission_classes = [IsVerifiedOrReadOnly, IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(who_added=user)
    

class UserProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    """Просматриваем, что именно добавлял юзер, его товары. Или удаляем"""
    
    permission_classes = [IsVerifiedOrReadOnly, IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(who_added=user)
    

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated, IsVerifiedOrReadOnly])
def to_like(request, product_id):
    
    """Удаляем или добавляем лайк"""
    
    user = request.user

    if request.method == 'POST':
        try:
            like = Likes.objects.create(user=user, product_id=product_id, is_liked=True)
            return Response({"detail": "Like added successfully."})
        except Exception as e:
            return Response({"detail": "Failed to add like.", "error": str(e)})
    
    elif request.method == 'DELETE':
        try:
            like = Likes.objects.get(user=user, product_id=product_id)
            like.delete()
            return Response({"detail": "Like removed successfully."})
        except Likes.DoesNotExist:
            return Response({"detail": "Like does not exist."}, status=404)
        
    
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsVerifiedOrReadOnly])
def liked_products(request):
    user = request.user
    liked_products = user.liked_products.all()
    
    serializer = ProductSerializer(liked_products, many=True)
    return Response(serializer.data)
