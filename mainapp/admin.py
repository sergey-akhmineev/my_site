from django.contrib import admin
from .models import Medicine, Category, Type, Subcategory, Order, OrderItem

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at', 'is_paid']
    list_editable = ['is_paid']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'medicine', 'quantity']


admin.site.register(Medicine)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Subcategory)