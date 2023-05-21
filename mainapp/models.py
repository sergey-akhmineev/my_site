from django.db import models

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
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