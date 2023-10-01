"""
URL configuration for django_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django_apiapp.views import OrderItemList, OrderItemDetail, UserList,ProductsByCategory, UserDetail,FavoriteDetail,FavoriteList,CommentDetail,CommentList,OrderDetail,OrderList,CategoryDetail,CategoryList,ProductById,ProductsByCategory,ProductDetail,ProductList

 
urlpatterns = [
    # URLs for 'OrderItem'
    path('order-items/', OrderItemList.as_view(), name='orderitem-list'),
    path('order-items/<int:pk>/', OrderItemDetail.as_view(), name='orderitem-detail'),
    
    # URLs for 'User'
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    # URLs for 'products' 
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('products/category/<str:category_name>/', ProductsByCategory.as_view(), name='product-by-category'),
  
    # URLs for 'Category'
    path('categories/', CategoryList.as_view(), name='category-list'),
    
    # URLs for 'Order'
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    
    # URLs for 'Comment'
    path('comments/', CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    
    # URLs for 'Favorite'
    path('favorites/', FavoriteList.as_view(), name='favorite-list'),
    path('favorites/<int:pk>/', FavoriteDetail.as_view(), name='favorite-detail'),
    
    # ... ajoutez d'autres URLs ici pour d'autres vues si nécessaire
]