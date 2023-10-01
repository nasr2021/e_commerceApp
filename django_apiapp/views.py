from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django_apiapp.serializers import productsSerializer,OrderSerializer,OrderItemSerializer,CommentSerializer,FavoriteSerializer,UserSerializer,CategorySerializer
from django_apiapp.models import products,Category, User, Order, Comment, Favorite, OrderItem
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# @csrf_exempt
# def studentApi(request, id=0):
#     if request.method == 'GET':
#         products_query = products.objects.all()  # Renommé en 'products_query'
#         student_serializer = productsSerializer(products_query, many=True)
#         return JsonResponse(student_serializer.data, safe=False)
#     elif request.method == 'POST':
#         student_data = JSONParser().parse(request)
#         student_serializer = productsSerializer(data=student_data)
#         if student_serializer.is_valid():
#             student_serializer.save()
#             return JsonResponse("Added Successfully", safe=False)
#         return JsonResponse("Failed to Add", safe=False)
#     elif request.method == 'PUT':
#         student_data = JSONParser().parse(request)
#         products_query = products.objects.get(id=id)  # Renommé en 'products_query'
#         student_serializer = productsSerializer(products_query, data=student_data)
#         if student_serializer.is_valid():
#             student_serializer.save()
#             return JsonResponse("Updated Successfully", safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method == 'DELETE':
#         products_query = products.objects.get(id=id)  # Renommé en 'products_query'
#         products_query.delete()
#         return JsonResponse("Deleted Successfully", safe=False)


# Views for 'products'
class ProductList(generics.ListCreateAPIView):
    queryset = products.objects.all()
    serializer_class = productsSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = products.objects.all()
    serializer_class = productsSerializer

# View to get products by category
class ProductsByCategory(generics.ListAPIView):
    serializer_class = productsSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']  # Utilisez 'category_name' au lieu de 'category_id'
        return products.objects.filter(category__name=category_name)

# View to get products by id
class ProductById(generics.RetrieveAPIView):
    queryset = products.objects.all()
    serializer_class = productsSerializer

# Views for 'Category'
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Views for 'Order'
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Views for 'Comment'
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Views for 'Favorite'
class FavoriteList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
# Views for 'OrderItem'
class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# Views for 'User'
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
