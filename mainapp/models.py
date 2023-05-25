from django.db import models
from userapp.models import MyUser

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    img = models.ImageField(upload_to='category', blank=True, null=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=32, unique=True)
    type = models.ManyToManyField(Type)
    category = models.ManyToManyField(Category)
    subcategory = models.ManyToManyField(Subcategory)
    description = models.TextField(blank=True, null=True)
    dosage = models.PositiveIntegerField(null=True, default=0, blank=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price = models.FloatField()
    availability = models.BooleanField(default=True)
    img = models.ImageField(upload_to='medicine', blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)

    def create_order(user, cart_items):
        order = Order(user=user)
        order.save()
        for item in cart_items:
            order_item = OrderItem(order=order, medicine=item.medicine, quantity=item.quantity)
            order_item.save()
        user.cart_items.clear()
        return order

    def __str__(self):
        return f'Заказ № {self.id}'

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.order_items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Медикамент"  ({self.medicine.name} количество: {self.quantity}) Заказ № {self.order.id}'

    def get_total_price(self):
        return self.medicine.price * self.quantity