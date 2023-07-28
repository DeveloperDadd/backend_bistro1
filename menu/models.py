from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null = True)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    name = models.CharField(max_length=50, null = True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    price = models.IntegerField(null=True, blank=True)
    spice_level = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete = models.CASCADE)
