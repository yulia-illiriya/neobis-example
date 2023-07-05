from django.urls import path
from .views import *
from .views import to_like, liked_products


urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('like/<int:product_id>/', to_like, name='like_or_unlike_product'),
    path('liked_products/', liked_products, name='list_of_liked_product'),
    path('users_added_product_list/', UserProductsView.as_view(), name="users_product"),
    path('users_added/<int:pk>/', UserProductDetailView.as_view(), name='users_detail_product')
]