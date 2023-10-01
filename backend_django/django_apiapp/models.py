from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class User(AbstractUser):
    
       
    first_name = models.CharField(max_length=30)  # Add field for first name
    last_name = models.CharField(max_length=30)   # Add field for last name
    email = models.EmailField(unique=True)         # Add field for email
    password = models.CharField(max_length=128)    # Password field (usually hashed)
    ConfirmPassword = models.CharField(max_length=128)  # Field for confirming password 
    groups = models.ManyToManyField(Group, related_name='admin', default=None)
    user_permissions = models.ManyToManyField(Permission, related_name='admin', default=None)

class products(models.Model):
    name = models.CharField(max_length=255, default='Default Name')
    description = models.TextField(default='Default Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='corps')
    image = models.ImageField(upload_to='products/', null=True, blank=True, default='products/default_image.jpg')
    def __str__(self):
        return self.name
    
    @property
    def category_name(self):
        return self.category.name if self.category else 'No Category'
        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')])

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
