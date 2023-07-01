from django.urls import path
from .views import PhotoListCreateView, PhotoRetrieveUpdateDestroyView, ProductListCreateView, ProductRetrieveUpdateDestroyView, PriceListCreateAPIView


urlpatterns = [
    path('price/', PriceListCreateAPIView.as_view(), name='price-list'),
    path('photos/', PhotoListCreateView.as_view(), name='photo-list'),
    path('photos/<int:pk>/', PhotoRetrieveUpdateDestroyView.as_view(), name='photo-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]