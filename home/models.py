from django.db import models

# Create your models here.
class Crackers(models.Model):
    cracker_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    Quantity = models.PositiveIntegerField()
    age_range = models.CharField(max_length=30)
    choices = [
        ('a',"Galoo"),
        ('n',"Bhumida")
    ] 
    type_of_cracker = models.CharField(max_length=1,choices=choices)
    image = models.ImageField(upload_to="Assets")


class Sweets(models.Model):
    s_name = models.CharField(max_length=100)
    s_price = models.PositiveIntegerField()
    s_quantity  = models.PositiveIntegerField()
    s_image = models.ImageField(upload_to="Assets")

class Gifts(models.Model):
    g_name = models.CharField(max_length=100)
    g_price = models.PositiveIntegerField()
    g_image = models.ImageField(upload_to="Assets")