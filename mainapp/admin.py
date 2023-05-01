from django.contrib import admin
from .models import Type, Category, Subcategory, Medicine

# Register your models here.

admin.site.register(Type)
admin.site.register(Subcategory)
admin.site.register(Medicine)
admin.site.register(Category)
