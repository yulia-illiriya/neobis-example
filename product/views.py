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
from drf_yasg import openapi
 

class ProductListCreateView(generics.ListCreateAPIView):
    """
    Product List API
    """
    swagger_tags = ['Product']
    
    permission_classes = [IsVerifiedOrReadOnly,]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
@swagger_auto_schema(tags=["Categories"])
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Product List API
    """
    swagger_tags = ['Product']
    
    permission_classes = [IsVerifiedOrReadOnly,]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class UserProductsView(generics.ListCreateAPIView):
    
    """"
    Product Added By User API
    """
    swagger_tags = ['Added_by_user']
    
    permission_classes = [IsVerifiedOrReadOnly, IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(who_added=user)
    

class UserProductDetailView(generics.RetrieveUpdateDestroyAPIView):
           
    """"
    Product Added By User API
    """
    swagger_tags = ['Added_by_user']
    
    permission_classes = [IsVerifiedOrReadOnly, IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(who_added=user)

@swagger_auto_schema(
    method='post',
    operation_description='Добавить лайк',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'product_id': openapi.Schema(type=openapi.TYPE_INTEGER),
        },
        required=['product_id'],
    ),
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'detail': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        400: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'detail': openapi.Schema(type=openapi.TYPE_STRING),
                'error': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
    },
)    
@swagger_auto_schema(
    method='delete',
    operation_description='Удалить лайк',
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'detail': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        404: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'detail': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
    },
)
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
        
@swagger_auto_schema(
    method='get',
    operation_description='Продукты, которые понравились',
    responses={200: ProductSerializer(many=True)},
)
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsVerifiedOrReadOnly])
def liked_products(request):
    
    """продукты, которые понравились"""
    
    user = request.user
    liked_products = user.liked_products.all()
    
    serializer = ProductSerializer(liked_products, many=True)
    return Response(serializer.data)
